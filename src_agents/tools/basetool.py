import os
from langchain_core.tools import tool
import pandas as pd
from logger import setup_logger
from typing import Dict, Optional, Annotated, List
from langgraph.prebuilt import InjectedState
from core.state import State
import io

logger = setup_logger()

@tool(
    "eda_data",
    description="Quick EDA over a CSV: head/info/describe/missing counts."
)
def eda_data(
    state: Annotated[State, InjectedState],
    data_path: Optional[str] = None
) -> str:
    # Ưu tiên tham số truyền vào; nếu không có, lấy từ state
    data_path = state.get("data_path") 
    if not data_path:
        raise ValueError(
            "Khong tim thay duong dan den du lieu: {data_path}"
        )
    logger.info(f"Attempting to read CSV file: {data_path}")

    try:
        df = pd.read_csv(data_path)
        info_buffer = io.StringIO()
        df.info(buf=info_buffer)
        # Lấy nội dung từ buffer bằng getvalue()
        info_str = info_buffer.getvalue()
        # --- KẾT THÚC SỬA LỖI ---

        head_str = df.head().to_string()
        describe_str = df.describe().to_string()
        missing_values_str = df.isnull().sum().to_string()

        # Tạo tóm tắt EDA dưới dạng một tin nhắn duy nhất
        eda_summary = f"""
        ### Tóm tắt Phân tích Khám phá (EDA) từ file {data_path} ###

        **1. 5 dòng dữ liệu đầu tiên:**
        {head_str}


        **2. Thông tin chung và Kiểu dữ liệu:**
        {info_str}


        **3. Thống kê mô tả (cho các cột số):**
        {describe_str}


        **4. Số lượng giá trị thiếu (Missing Values):**
        {missing_values_str}

        """
        logger.info(f"Successfully read CSV file ")
        return eda_summary
    except Exception as e:
        logger.warning(f"Read file error: {e}")
    raise ValueError("Unable to read file with provided encodings")
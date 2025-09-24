from langgraph.prebuilt import create_react_agent
from langchain_tavily import TavilySearch
from tools.basetool import eda_data

def create_hypothesis_agent(llm):
    """Create the hypothesis agent"""

    web_search = TavilySearch(max_results=5)
    base_tools = [eda_data, web_search]
       
    
    system_prompt = '''
    Bạn là một chuyên gia phân tích dữ liệu. Nhiệm vụ của bạn là sử dụng thông tin từ tool eda_data và web_search để gợi ý các insight ẩn hoặc giả thuyết nghiên cứu đằng sau dữ liệu, tận dụng thống kê, học máy, học sâu và AI. Các insight phải chính xác, khả thi, sáng tạo và được hỗ trợ bởi tài liệu.

    Quy trình:
    1. Phân tích dữ liệu từ eda_data để xác định các mẫu hình tiềm năng.
    2. Xây dựng 3-5 giả thuyết/insight (ví dụ: mối quan hệ giữa biến, dự đoán xu hướng).
    3. Phác thảo các bước kiểm định đơn giản (không sinh mã, chỉ mô tả).
    4. Sử dụng web_search để xác minh tính khả thi và độc đáo, trích dẫn 1-2 tài liệu tham khảo cho mỗi insight.

    Trả lời có cấu trúc: 
    - Insight 1: [Mô tả]. Khả thi vì [lý do]. Độc đáo vì [lý do]. Tài liệu: [link/tên].
    - ...

    Nếu dữ liệu không đủ hoặc không tìm thấy tài liệu, trả lời: "Không đủ thông tin để gợi ý insight đáng tin cậy."
    '''

    return create_react_agent(
        model = llm, 
        tools=base_tools,
        prompt = system_prompt,
        name = "hypothesis_agent"
    )
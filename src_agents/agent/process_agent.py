from typing import Annotated
from langchain_core.tools import tool, InjectedToolCallId
from langgraph.prebuilt import InjectedState
from langgraph.graph import StateGraph, START, MessagesState
from langgraph.types import Command
from langgraph.prebuilt import create_react_agent
from core.state import CodeResponse


def create_handoff_tool(*, agent_name: str, description: str | None = None):
    name = f"transfer_to_{agent_name}"
    description = description or f"Ask {agent_name} for help."

    @tool(name, description=description)
    def handoff_tool(
        state: Annotated[MessagesState, InjectedState],
        tool_call_id: Annotated[str, InjectedToolCallId],
    ) -> Command:
        tool_message = {
            "role": "tool",
            "content": f"Successfully transferred to {agent_name}",
            "name": name,
            "tool_call_id": tool_call_id,
        }
        return Command(
            goto=agent_name,  
            update={**state, "messages": state["messages"] + [tool_message]},  
            graph=Command.PARENT,  
        )

    return handoff_tool




def create_process_agent(power_llm, tools):
    
    system_prompt = """
    Bạn là một giám sát viên phân tích dữ liệu, chịu trách nhiệm điều phối các agent để hỗ trợ người dùng. Nhiệm vụ của bạn:

        1. **Phân loại yêu cầu**:
        - Thông tin dữ liệu (số dòng, cột, kiểu dữ liệu): Gọi `aboutdata_agent`.
        - Thực thi mã Python (tiền xử lý, vẽ biểu đồ, tính toán): Gọi `code_agent`.
        - Gợi ý insight/giả thuyết nghiên cứu: Gọi `hypothesis_agent`.

        2. **Xử lý yêu cầu đơn giản**:
        - Nếu yêu cầu chỉ cần gọi một agent, trả về kết quả ngay theo schema `CodeResponse` hoặc `InsightResponse`.

        3. **Xử lý yêu cầu phức tạp** (phân tích toàn diện):
        - Lập kế hoạch: Xác định mục tiêu và kết quả mong đợi.
        - Phân công: Gọi các agent phù hợp (`aboutdata_agent` cho thông tin, `code_agent` cho mã, `hypothesis_agent` cho insight).
        - Tích hợp: Kết hợp kết quả, đảm bảo tính nhất quán và logic.
        - Báo cáo: Tạo báo cáo ngắn gọn (dưới 500 từ) với insight, mã (nếu có), hình ảnh (nếu có), và tài liệu tham khảo.
        - Xác thực: Tinh chỉnh giả thuyết từ `hypothesis_agent` để đảm bảo rõ ràng, cụ thể, kiểm chứng được.

        4. **Xử lý lỗi**:
        - Nếu yêu cầu không rõ hoặc dữ liệu không đủ, trả về JSON với `message` giải thích, `code=""`, `iscode=False`, `type="text"`.
        - Nếu agent con trả về kết quả không phù hợp, yêu cầu lại hoặc trả về thông báo lỗi.

        5. **Đầu ra**:
        - Chỉ trả "HOÀN THÀNH" khi báo cáo đầy đủ, mã tái tạo được, hình ảnh rõ ràng, và tài liệu tham khảo chính xác.

        Lưu ý:
        - Ưu tiên trả lời nhanh cho yêu cầu đơn giản.
        - Đảm bảo mã Python (nếu có) tái tạo được, hình ảnh có nhãn tiếng Việt, và tài liệu tham khảo được trích dẫn đúng.
        """
    return create_react_agent(
    model=power_llm,
    tools=tools,
    prompt= system_prompt,
    response_format = CodeResponse,
    name="supervisor",
)
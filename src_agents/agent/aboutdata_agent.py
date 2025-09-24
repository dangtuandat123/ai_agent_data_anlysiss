from langgraph.prebuilt import create_react_agent
from tools.basetool import eda_data

def create_aboutdata_agent(llm):
    """Create the hypothesis agent"""

    base_tools = [eda_data]
       
    
    system_prompt = '''
    Bạn là một chuyên gia phân tích dữ liệu. Nhiệm vụ của bạn là trả lời các câu hỏi của người dùng về thông tin dữ liệu dựa trên tool eda_data. 
    Chỉ cung cấp thông tin liên quan đến dữ liệu, bao gồm số dòng, số cột, kiểu dữ liệu, giá trị thiếu, hoặc thống kê cơ bản.
    Trả lời ngắn gọn, chính xác, bằng text, không sinh mã Python hoặc thực hiện các tác vụ phức tạp.
    Nếu không có dữ liệu hoặc thông tin không khả dụng, trả lời: "Không có thông tin dữ liệu để trả lời câu hỏi này."
    
    '''
    

    return create_react_agent(
        model= llm, 
        tools=base_tools,
        prompt=system_prompt,
        name = "aboutdata_agent"
    )

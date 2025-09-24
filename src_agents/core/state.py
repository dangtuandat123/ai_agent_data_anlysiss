from langchain_core.messages import BaseMessage
from typing_extensions import Sequence, TypedDict, Annotated, List
from pydantic import BaseModel, Field
from langgraph.graph.message import add_messages


class State(TypedDict):
    """TypedDict for the entire state structure."""
    # The sequence of messages exchanged in the conversation
    messages: Annotated[List[BaseMessage], add_messages]
    data_path: str = ""

    query: str = ""

    # The complete content of the research hypothesis
   

class NoteState(BaseModel):
    """Pydantic model for the entire state structure."""
    messages: Sequence[BaseMessage] = Field(default_factory=list, description="List of message dictionaries")
    hypothesis: str = Field(default="", description="Current research hypothesis")
    process: str = Field(default="", description="Current research process")
    process_decision: str = Field(default="", description="Decision about the next process step")
    visualization_state: str = Field(default="", description="Current state of data visualization")
    searcher_state: str = Field(default="", description="Current state of the search process")
    code_state: str = Field(default="", description="Current state of code development")
    report_section: str = Field(default="", description="Content of the report sections")
    quality_review: str = Field(default="", description="Feedback from quality review")
    needs_revision: bool = Field(default=False, description="Flag indicating if revision is needed")
    sender: str = Field(default="", description="Identifier of the last message sender")

    class Config:
        arbitrary_types_allowed = True  # Allow BaseMessage type without explicit validator


class CodeResponse(BaseModel):
    """Schema để định dạng câu trả lời cuối cùng của AI."""
    message: str = Field(description="Một lời giải thích hoặc tin nhắn thân thiện, súc tích cho người dùng.")
    code: str = Field(
        description="Một đoạn mã Python hoàn chỉnh nếu cần thiết để trả lời yêu cầu. Trả về chuỗi rỗng nếu không có code.")
    iscode: bool = Field(description="Trả về True nếu có đoạn mã trong trường 'code', ngược lại trả về False.")
    type: str = Field(
        description="Xác định loại output: 'text' (chỉ văn bản), 'img' (nếu code tạo ra đồ thị/hình ảnh), hoặc 'table_html' (nếu code tạo ra bảng dạng HTML).")



import os
from typing import Dict, Any
from logger import setup_logger
from langchain_core.messages import HumanMessage
from core.workflow import WorkflowManager
from core.language_models import LanguageModelManager
from dotenv import load_dotenv

load_dotenv
class MultiAgentSystem:
    def __init__(self):
        self.logger = setup_logger()
        self.lm_manager = LanguageModelManager()
        self.workflow_manager = WorkflowManager(
            language_models=self.lm_manager.get_models(),
        )


    def run(self, user_query: str, csv_path: str, thread_id: str = "demo-1"):
        """Khởi chạy graph với state ban đầu gồm messages + data_path"""
        graph = self.workflow_manager.get_graph()
#         graph.get_graph().print_ascii()

# # Xuất Mermaid
#         print(graph.get_graph().draw_mermaid())

#         # Lưu PNG
#         with open("workflow.png", "wb") as f:
#             f.write(graph.get_graph().draw_mermaid_png())

        initial_state = {
            "messages": [HumanMessage(content=user_query)],
            "data_path": csv_path,     # tool EDA sẽ đọc từ đây
            "query": user_query        # nếu State của bạn dùng tới
        }

        # Stream toàn bộ state sau mỗi node (dễ debug)
        for state in graph.stream(
            initial_state,
            {"configurable": {"thread_id": thread_id}},
            stream_mode="values"
        ):
            msgs = state.get("messages", [])
            if msgs:
                last = msgs[-1]
                # In nhanh nội dung tin nhắn cuối cùng (tùy ý)
                try:
                    print(f"[{last.type}] {last.content}")
                except Exception:
                    print(repr(last))

        # Lấy snapshot state cuối cùng (nếu cần kiểm tra kết quả)
        final = graph.get_state({"configurable": {"thread_id": thread_id}})
        self.logger.info("Ket thuc. Cac key trong state cuoi: %s", list(final.values.keys()))
        return final

def main():
    """Main entry point"""
    system = MultiAgentSystem()
    
    # Example usage
    system.run(
        user_query="Vẽ biểu đồ thể hiện số đơn hàng theo từng region, đường dẫn đến file là:'synthetic_ecommerce_data.csv' ",
        csv_path="synthetic_ecommerce_data.csv",
        thread_id="demo-1"
    )

if __name__ == "__main__":
    main()

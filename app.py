from graph import graph
from rag.retriever import get_retriever


def main():

    print("=" * 60)
    print("ABC Technologies Customer Support")
    print("=" * 60)

    customer_name = input("Enter Customer Name: ")

    retriever = get_retriever()

    while True:

        query = input("\nCustomer: ")

        if query.lower() in ["exit", "quit"]:
            break

        docs = retriever.invoke(query)

        context = [
            doc.page_content
            for doc in docs
        ]

        state = {

            "customer_name": customer_name,

            "query": query,

            "intent": "",

            "department": "",

            "retrieved_context": context,

            "agent_response": "",

            "final_response": "",

            "requires_approval": False,

            "approval_status": "",

            "conversation_history": []

        }

        result = graph.invoke(state)

        print("\n" + "=" * 60)
        print("Final Response")
        print("=" * 60)

        print(result["final_response"])


if __name__ == "__main__":
    main()
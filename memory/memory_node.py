from memory.database import save_conversation, get_last_query


def memory_node(state):
    """
    Save conversations to SQLite.
    Handle memory recall queries.
    """

    customer = state["customer_name"]

    # Memory Recall
    if state["intent"] == "Memory":

        previous_query = get_last_query(customer)

        if previous_query:
            state["final_response"] = (
                f"Your previous support issue was:\n\n{previous_query}"
            )
        else:
            state["final_response"] = (
                "I couldn't find any previous conversations."
            )

        return state

    # Save current conversation
    save_conversation(
        customer,
        state["query"],
        state["final_response"]
    )

    return state
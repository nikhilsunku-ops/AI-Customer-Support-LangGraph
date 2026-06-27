def human_approval(state):
    """
    Simulated Human Approval Node.
    """

    print("\n" + "=" * 60)
    print("HUMAN APPROVAL REQUIRED")
    print("=" * 60)

    print("\nCustomer Query:")
    print(state["query"])

    print("\nAgent Response:")
    print(state["agent_response"])

    while True:

        decision = input(
            "\nApprove this request? (yes/no): "
        ).strip().lower()

        if decision in ["yes", "y"]:

            state["approval_status"] = "Approved"

            break

        elif decision in ["no", "n"]:

            state["approval_status"] = "Rejected"

            state["agent_response"] = (
                "Your request has been reviewed and was not approved "
                "by the supervisor."
            )

            break

        else:

            print("Please enter yes or no.")

    return state
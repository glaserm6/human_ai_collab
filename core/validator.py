def validate_code(user_code, phase):
    """
    Validates the user's Python code for each phase.
    """

    try:
        local_env = {}

        # Execute the user code safely
        exec(user_code, {}, local_env)

        # -------------------------
        # PHASE 1
        # -------------------------
        if phase == 1:

            if "square" not in local_env:
                return False

            func = local_env["square"]

            return (
                func(2) == 4 and
                func(3) == 9 and
                func(5) == 25
            )

        # -------------------------
        # PHASE 2
        # -------------------------
        elif phase == 2:

            if "add_numbers" not in local_env:
                return False

            func = local_env["add_numbers"]

            return (
                func(2, 3) == 5 and
                func(-1, 1) == 0 and
                func(10, 5) == 15
            )

        # -------------------------
        # PHASE 3
        # -------------------------
        elif phase == 3:

            if "factorial" not in local_env:
                return False

            func = local_env["factorial"]

            return (
                func(3) == 6 and
                func(4) == 24 and
                func(5) == 120
            )

        return False

    except Exception:
        return False
def generate_code(ui_spec):
    code = []
    for comp in ui_spec.get("components", []):
        code.append(f"<{comp} />")
    return "\n".join(code)

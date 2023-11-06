def test_alchemy_combine():

    # Prueba para crear oro
    oven = make_oven()
    result = alchemy_combine(oven, ["lead", "mercury"], 5000)
    assert result == "gold", f"Error: {result}"

    # Prueba para crear nieve
    oven = make_oven()
    result = alchemy_combine(oven, ["water", "air"], -100)
    assert result == "snow", f"Error: {result}"

    # Prueba para crear pizza
    oven = make_oven()
    result = alchemy_combine(oven, ["cheese", "dough", "tomato"], 150)
    assert result == "pizza", f"Error: {result}"

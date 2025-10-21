def walk2d():
    var = yield (0,0)
    while var:
        var = yield f"<{var}>"
        
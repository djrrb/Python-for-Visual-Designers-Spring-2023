bp = BezierPath()
bp.rect(0, 0, 50, 50)


bp2 = BezierPath()
bp2.polygon(
    (0, 0),
    (50, 0),
    (0, 75)
    )

bp3 = BezierPath()
bp3.polygon(
   (25, 0), 
    (25, 50),
    (-20, 50), 
    )


bp4 = bp.union(bp2)
bp5 = bp3.union(bp4)


translate(260)
scale(9)
drawPath(bp5)

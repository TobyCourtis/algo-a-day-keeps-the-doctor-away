from cairosvg import svg2png

svg_code = open("./originals/text_effects.svg", 'rt').read()
svg2png(bytestring=svg_code, write_to='output.png')

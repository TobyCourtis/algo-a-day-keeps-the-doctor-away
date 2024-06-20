from cairosvg import svg2png

svg_code = open("example.svg", 'rt').read()
svg2png(bytestring=svg_code, write_to='output.png')

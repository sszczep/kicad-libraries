import os

sizesToGenerate=["1.00", "1.25", "1.50", "1.75", "2.00", "2.25", "2.50", "2.75", "3.00", "4.00", "4.50", "5.50", "6.00", "6.25", "6.50", "7.00", "8.00", "9.00", "9.75", "10.00"]

# All of the dimensions are in mm
unit = 19.05

# Spacings taken from https://cdn.sparkfun.com/datasheets/Components/Switches/MX%20Series.pdf and https://deskthority.net/wiki/Space_bar_dimensions
stabSpacings = {
  "2.00": 0.94*25.4,
  "2.25": 0.94*25.4,
  "2.50": 0.94*25.4,
  "2.75": 0.94*25.4,
  "3.00": 1.5*25.4,
  "4.00": 2.25*25.4,
  "4.50": 2.73*25.4,
  "5.50": 3.375*25.4,
  "6.00": 3*25.4,
  "6.25": 100,
  "6.50": 4.125*25.4,
  "7.00": 4.5*25.4,
  "8.00": 5.25*25.4,
  "9.00": 5.25*25.4,
  "9.75": 5.25*25.4,
  "10.00": 5.25*25.4,
}

componentsList = {
  "BaseStart": """
(module {name} (layer F.Cu) (tedit 5E866FEB)
  (descr "{description}")
  (tags "{keywords}")
  (fp_text reference REF** (at 0 -8.6625) (layer F.SilkS)
    (effects (font (size 1 1) (thickness 0.15)))
  )
  (fp_text value {name} (at 0 8.6625) (layer F.Fab)
    (effects (font (size 1 1) (thickness 0.15)))
  )
  (fp_line (start 7 7) (end -7 7) (layer F.SilkS) (width 0.12))
  (fp_line (start 7 -7) (end 7 7) (layer F.SilkS) (width 0.12))
  (fp_line (start -7 -7) (end 7 -7) (layer F.SilkS) (width 0.12))
  (fp_line (start -7 -7) (end -7 7) (layer F.SilkS) (width 0.12))
  (fp_line (start -7.8 -7.8) (end 7.8 -7.8) (layer F.Fab) (width 0.12))
  (fp_line (start -7.8 -7.8) (end -7.8 7.8) (layer F.Fab) (width 0.12))
  (fp_line (start 7.8 -7.8) (end 7.8 7.8) (layer F.Fab) (width 0.12))
  (fp_line (start -7.8 7.8) (end 7.8 7.8) (layer F.Fab) (width 0.12))
  (fp_line (start -{outlineSize} 9.525) (end -{outlineSize} -9.525) (layer Dwgs.User) (width 0.12))
  (fp_line (start {outlineSize} 9.525) (end -{outlineSize} 9.525) (layer Dwgs.User) (width 0.12))
  (fp_line (start {outlineSize} -9.525) (end {outlineSize} 9.525) (layer Dwgs.User) (width 0.12))
  (fp_line (start -{outlineSize} -9.525) (end {outlineSize} -9.525) (layer Dwgs.User) (width 0.12))
  (pad "" np_thru_hole circle (at 0 0) (size 4 4) (drill 4) (layers *.Cu *.Mask))""",

  "Pins": """
  (pad 1 thru_hole circle (at -3.81 -2.54) (size 2.2 2.2) (drill 1.5) (layers *.Cu *.Mask))
  (pad 2 thru_hole circle (at 2.54 -5.08) (size 2.2 2.2) (drill 1.5) (layers *.Cu *.Mask))""",

  "PCB": """
  (pad "" np_thru_hole circle (at -5.08 0) (size 1.7 1.7) (drill 1.7) (layers *.Cu *.Mask))
  (pad "" np_thru_hole circle (at 5.08 0) (size 1.7 1.7) (drill 1.7) (layers *.Cu *.Mask))""",

  "KailhSocket": """
  (pad "" np_thru_hole circle (at -3.81 -2.54) (size 3 3) (drill 3) (layers *.Cu *.Mask))
  (pad "" np_thru_hole circle (at 2.54 -5.08) (size 3 3) (drill 3) (layers *.Cu *.Mask))
  (pad 1 smd rect (at -7.41 -2.54) (size 2.55 2.5) (layers B.Cu B.Paste B.Mask))
  (pad 2 smd rect (at 6.015 -5.08) (size 2.55 2.5) (layers B.Cu B.Paste B.Mask))
  (model "${{KIPRJMOD}}/models/KailhSocket.stp"
    (offset (xyz -0.6 3.8 -3.5))
    (scale (xyz 1 1 1))
    (rotate (xyz 0 0 180))
  )""",

  "LED": """
  (pad 3 thru_hole circle (at -1.27 5.08) (size 1.6906 1.6906) (drill 0.9906) (layers *.Cu *.Mask))
  (pad 4 thru_hole circle (at 1.27 5.08) (size 1.6906 1.6906) (drill 0.9906) (layers *.Cu *.Mask))""",

  "LTST-A683CEGBW": """
  (fp_line (start -1.7 3.25) (end -2 3.25) (layer B.SilkS) (width 0.12))
  (fp_line (start -2 3.25) (end -2 3.55) (layer B.SilkS) (width 0.12))
  (fp_line (start -1.7 3.55) (end 1.7 3.55) (layer Edge.Cuts) (width 0.05))
  (fp_line (start 1.7 3.55) (end 1.7 6.55) (layer Edge.Cuts) (width 0.05))
  (fp_line (start 1.7 6.55) (end -1.7 6.55) (layer Edge.Cuts) (width 0.05))
  (fp_line (start -1.7 6.55) (end -1.7 3.55) (layer Edge.Cuts) (width 0.05))
  (pad 3 smd rect (at -2.6 4.3) (size 1.8 0.9) (layers B.Cu B.Paste B.Mask))
  (pad 4 smd rect (at -2.6 5.8) (size 1.8 0.9) (layers B.Cu B.Paste B.Mask))
  (pad 5 smd rect (at 2.6 4.3) (size 1.8 0.9) (layers B.Cu B.Paste B.Mask))
  (pad 6 smd rect (at 2.6 5.8) (size 1.8 0.9) (layers B.Cu B.Paste B.Mask))
  (model "${{KIPRJMOD}}/models/LTST-A683CEGBW.step"
    (offset (xyz 0 -5.05 -1.87))
    (scale (xyz 1 1 1))
    (rotate (xyz 0 0 0))
  )""",

  "LTST-A683CEGBW-Rotated": """
  (fp_line (start 1.7 6.85) (end 2 6.85) (layer B.SilkS) (width 0.12))
  (fp_line (start 2 6.85) (end 2 6.55) (layer B.SilkS) (width 0.12))
  (fp_line (start -1.7 3.55) (end 1.7 3.55) (layer Edge.Cuts) (width 0.05))
  (fp_line (start 1.7 3.55) (end 1.7 6.55) (layer Edge.Cuts) (width 0.05))
  (fp_line (start 1.7 6.55) (end -1.7 6.55) (layer Edge.Cuts) (width 0.05))
  (fp_line (start -1.7 6.55) (end -1.7 3.55) (layer Edge.Cuts) (width 0.05))
  (pad 3 smd rect (at 2.6 5.8 180) (size 1.8 0.9) (layers B.Cu B.Paste B.Mask))
  (pad 4 smd rect (at 2.6 4.3 180) (size 1.8 0.9) (layers B.Cu B.Paste B.Mask))
  (pad 5 smd rect (at -2.6 5.8 180) (size 1.8 0.9) (layers B.Cu B.Paste B.Mask))
  (pad 6 smd rect (at -2.6 4.3 180) (size 1.8 0.9) (layers B.Cu B.Paste B.Mask))
  (model "${{KIPRJMOD}}/models/LTST-A683CEGBW.step"
    (offset (xyz 0 -5.05 -1.87))
    (scale (xyz 1 1 1))
    (rotate (xyz 0 0 180))
  )""",

  "StabWireTop": """
  (pad "" np_thru_hole circle (at -{stabSpacing} 7) (size 3.05 3.05) (drill 3.05) (layers *.Cu *.Mask))
  (pad "" np_thru_hole circle (at -{stabSpacing} -8.24) (size 4 4) (drill 4) (layers *.Cu *.Mask))
  (pad "" np_thru_hole circle (at {stabSpacing} -8.24) (size 4 4) (drill 4) (layers *.Cu *.Mask))
  (pad "" np_thru_hole circle (at {stabSpacing} 7) (size 3.05 3.05) (drill 3.05) (layers *.Cu *.Mask))""",

  "StabWireBottom": """
  (pad "" np_thru_hole circle (at -{stabSpacing} -7) (size 3.05 3.05) (drill 3.05) (layers *.Cu *.Mask))
  (pad "" np_thru_hole circle (at -{stabSpacing} 8.24) (size 4 4) (drill 4) (layers *.Cu *.Mask))
  (pad "" np_thru_hole circle (at {stabSpacing} 8.24) (size 4 4) (drill 4) (layers *.Cu *.Mask))
  (pad "" np_thru_hole circle (at {stabSpacing} -7) (size 3.05 3.05) (drill 3.05) (layers *.Cu *.Mask))""",

  "BaseEnd": """
)"""
}

# Possible variants:
# 1: Plate/PCB mounted
# 2: Stabilizer Plate/PCB mounted
# 3: no LED/LED/LTST-A683CEGBW
# 4: Normal switch mount/Kail Socket for hot-swap compatibility

variantsList = [
  ("Plate", ["BaseStart", "Pins", "BaseEnd"]),
  ("Plate_StabWireTop", ["BaseStart", "Pins", "StabWireTop", "BaseEnd"]),
  ("Plate_StabWireBottom", ["BaseStart", "Pins", "StabWireBottom", "BaseEnd"]),
  ("Plate_LED", ["BaseStart", "Pins", "LED", "BaseEnd"]),
  ("Plate_StabWireTop_LED", ["BaseStart", "Pins", "StabWireTop", "LED", "BaseEnd"]),
  ("Plate_StabWireBottom_LED", ["BaseStart", "Pins", "StabWireBottom", "LED", "BaseEnd"]),
  ("Plate_LTST-A683CEGBW", ["BaseStart", "Pins", "LTST-A683CEGBW", "BaseEnd"]),
  ("Plate_LTST-A683CEGBW-Rotated", ["BaseStart", "Pins", "LTST-A683CEGBW-Rotated", "BaseEnd"]),
  ("Plate_StabWireTop_LTST-A683CEGBW", ["BaseStart", "Pins", "StabWireTop", "LTST-A683CEGBW", "BaseEnd"]),
  ("Plate_StabWireBottom_LTST-A683CEGBW", ["BaseStart", "Pins", "StabWireBottom", "LTST-A683CEGBW", "BaseEnd"]),
  ("Plate_StabWireTop_LTST-A683CEGBW-Rotated", ["BaseStart", "Pins", "StabWireTop", "LTST-A683CEGBW-Rotated", "BaseEnd"]),
  ("Plate_StabWireBottom_LTST-A683CEGBW-Rotated", ["BaseStart", "Pins", "StabWireBottom", "LTST-A683CEGBW-Rotated", "BaseEnd"]),
  ("Plate_KailhSocket", ["BaseStart", "KailhSocket", "BaseEnd"]),
  ("Plate_KailhSocket_StabWireTop", ["BaseStart", "KailhSocket", "StabWireTop", "BaseEnd"]),
  ("Plate_KailhSocket_StabWireBottom", ["BaseStart", "KailhSocket", "StabWireBottom", "BaseEnd"]),
  ("Plate_KailhSocket_LED", ["BaseStart", "KailhSocket", "LED", "BaseEnd"]),
  ("Plate_KailhSocket_StabWireTop_LED", ["BaseStart", "KailhSocket", "StabWireTop", "LED", "BaseEnd"]),
  ("Plate_KailhSocket_StabWireBottom_LED", ["BaseStart", "KailhSocket", "StabWireBottom", "LED", "BaseEnd"]),
  ("Plate_KailhSocket_LTST-A683CEGBW", ["BaseStart", "KailhSocket", "LTST-A683CEGBW", "BaseEnd"]),
  ("Plate_KailhSocket_LTST-A683CEGBW-Rotated", ["BaseStart", "KailhSocket", "LTST-A683CEGBW-Rotated", "BaseEnd"]),
  ("Plate_KailhSocket_StabWireTop_LTST-A683CEGBW", ["BaseStart", "KailhSocket", "StabWireTop", "LTST-A683CEGBW", "BaseEnd"]),
  ("Plate_KailhSocket_StabWireBottom_LTST-A683CEGBW", ["BaseStart", "KailhSocket", "StabWireBottom", "LTST-A683CEGBW", "BaseEnd"]),
  ("Plate_KailhSocket_StabWireTop_LTST-A683CEGBW-Rotated", ["BaseStart", "KailhSocket", "StabWireTop", "LTST-A683CEGBW-Rotated", "BaseEnd"]),
  ("Plate_KailhSocket_StabWireBottom_LTST-A683CEGBW-Rotated", ["BaseStart", "KailhSocket", "StabWireBottom", "LTST-A683CEGBW-Rotated", "BaseEnd"]),
  ("PCB", ["BaseStart", "Pins", "PCB", "BaseEnd"]),
  ("PCB_StabWireTop", ["BaseStart", "Pins", "PCB", "StabWireTop", "BaseEnd"]),
  ("PCB_StabWireBottom", ["BaseStart", "Pins", "PCB", "StabWireBottom", "BaseEnd"]),
  ("PCB_LED", ["BaseStart", "Pins", "PCB", "LED", "BaseEnd"]),
  ("PCB_StabWireTop_LED", ["BaseStart", "Pins", "PCB", "StabWireTop", "LED", "BaseEnd"]),
  ("PCB_StabWireBottom_LED", ["BaseStart", "Pins", "PCB", "StabWireBottom", "LED", "BaseEnd"]),
  ("PCB_LTST-A683CEGBW", ["BaseStart", "Pins", "PCB", "LTST-A683CEGBW", "BaseEnd"]),
  ("PCB_LTST-A683CEGBW-Rotated", ["BaseStart", "Pins", "PCB", "LTST-A683CEGBW-Rotated", "BaseEnd"]),
  ("PCB_StabWireTop_LTST-A683CEGBW", ["BaseStart", "Pins", "PCB", "StabWireTop", "LTST-A683CEGBW", "BaseEnd"]),
  ("PCB_StabWireBottom_LTST-A683CEGBW", ["BaseStart", "Pins", "PCB", "StabWireBottom", "LTST-A683CEGBW", "BaseEnd"]),
  ("PCB_StabWireTop_LTST-A683CEGBW-Rotated", ["BaseStart", "Pins", "PCB", "StabWireTop", "LTST-A683CEGBW-Rotated", "BaseEnd"]),
  ("PCB_StabWireBottom_LTST-A683CEGBW-Rotated", ["BaseStart", "Pins", "PCB", "StabWireBottom", "LTST-A683CEGBW-Rotated", "BaseEnd"]),
  ("PCB_KailhSocket", ["BaseStart", "KailhSocket", "PCB", "BaseEnd"]),
  ("PCB_KailhSocket_StabWireTop", ["BaseStart", "KailhSocket", "PCB", "StabWireTop", "BaseEnd"]),
  ("PCB_KailhSocket_StabWireBottom", ["BaseStart", "KailhSocket", "PCB", "StabWireBottom", "BaseEnd"]),
  ("PCB_KailhSocket_LED", ["BaseStart", "KailhSocket", "PCB", "LED", "BaseEnd"]),
  ("PCB_KailhSocket_StabWireTop_LED", ["BaseStart", "KailhSocket", "PCB", "StabWireTop", "LED", "BaseEnd"]),
  ("PCB_KailhSocket_StabWireBottom_LED", ["BaseStart", "KailhSocket", "PCB", "StabWireBottom", "LED", "BaseEnd"]),
  ("PCB_KailhSocket_LTST-A683CEGBW", ["BaseStart", "KailhSocket", "PCB", "LTST-A683CEGBW", "BaseEnd"]),
  ("PCB_KailhSocket_LTST-A683CEGBW-Rotated", ["BaseStart", "KailhSocket", "PCB", "LTST-A683CEGBW-Rotated", "BaseEnd"]),
  ("PCB_KailhSocket_StabWireTop_LTST-A683CEGBW", ["BaseStart", "KailhSocket", "PCB", "StabWireTop", "LTST-A683CEGBW", "BaseEnd"]),
  ("PCB_KailhSocket_StabWireBottom_LTST-A683CEGBW", ["BaseStart", "KailhSocket", "PCB", "StabWireBottom", "LTST-A683CEGBW", "BaseEnd"]),
  ("PCB_KailhSocket_StabWireTop_LTST-A683CEGBW-Rotated", ["BaseStart", "KailhSocket", "PCB", "StabWireTop", "LTST-A683CEGBW-Rotated", "BaseEnd"]),
  ("PCB_KailhSocket_StabWireBottom_LTST-A683CEGBW-Rotated", ["BaseStart", "KailhSocket", "PCB", "StabWireBottom", "LTST-A683CEGBW-Rotated", "BaseEnd"]),
]

def generateFootprint(variant, size):
  (name, components) = variant
  
  name = f"CherryMX_{size}u_{name}"

  mountType = "PCB" if "PCB" in components else "Plate"
  usingKailhSocket = "yes" if "KailhSocket" in components else "no"
  stabilizer = ("n/a" if float(size) < 2 else ("PCB mounted (Wire Top)" if "StabWireTop" in components else ("PCB mounted (Wire Bottom)" if "StabWireBottom" in components else "Plate mounted")))
  lighting = ("LTST-A683CEGBW" if "LTST-A683CEGBW" in components else ("LTST-A683CEGBW (rotated)" if "LTST-A683CEGBW-Rotated" in components else ("2 pin LED" if "LED" in components else "none")))

  description = "Cherry MX switch footprint. "
  description += f"Size: {size}u"
  description += f", Mount type: {mountType}"
  description += f", Using Kailh Socket: {usingKailhSocket}"
  description += f", Stabilizer: {stabilizer}"
  description += f", Lighting: {lighting}"

  keywords = name.replace("_", " ")

  code = ""
  for component in components:
    code += componentsList[component].format(
      name=name, 
      description=description, 
      keywords=keywords, 
      outlineSize=float(size) * unit / 2, 
      stabSpacing=stabSpacings[size] / 2 if size in stabSpacings else "",
    )

  return (name, code)

for variant in variantsList:
  dirname = f"CherryMX_{variant[0]}.pretty"
  os.makedirs(dirname, exist_ok=True)

  for size in sizesToGenerate:
    if ("StabWireTop" in variant[1] or "StabWireBottom" in variant[1]) and size not in stabSpacings:
      continue

    (name, code) = generateFootprint(variant, size)
    file = open(f"{dirname}/{name}.kicad_mod", "w+")
    file.writelines(code)
    file.close()

    print(f"Generated: {name}.kicad_mod")

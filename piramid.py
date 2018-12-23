def hitung_luas(sisi=0, alas=0, tinggi=0):
    "fungsi menghitung luas dari limas"
    lim = sisi*sisi+4*0.5*alas*tinggi
    return (lim)

print "<!DOCTYPE html>"
print
print """<html>	
	<head><title>Praktikum kg  3</title></head>
	<body>"""
print """		<form>
		<table border="0">
			<tr>
				<td rowspan= "0"><td>
				<td><font color="black" size="8"><b>Bangun Geometri</b></font></td>
			</tr>"""
print """			<tr>
				<td rowspan="11"><img src= "bg.png" width = "180" height="180"></td>
				<td><font color="black" size="3">Nama bangun :</font></td>
				<td><font color="black" size="3">Piramid</font></td>
			</tr>"""
print """			<tr>
				<td><font color="black" size="3">Dimensi(2D/3D) :</font></td>
				<td><font color="black" size="3">3D</font></td>
			</tr>"""
print """			<tr>
				<td><font color="black" size="3">Rumus luas :</font></td>
				<td><font color="black" size="3">sisi x sisi + 4 x 0.5 x alas x tinggi</font></td>
			</tr>"""
print """			<tr>
				<td><font color="black" size="3">Parameter 1 :</font></td>
				<td><font color="black" size="3">Sisi</font></td>
			</tr>"""
print """			<tr>
				<td><font color="black" size="3">Parameter 2 :</font></td>
				<td><font color="black" size="3">Alas</font></td>
			</tr>"""
print """			<tr>
				<td><font color="black" size="3">Parameter 3 :</font></td>
				<td><font color="black" size="3">Tinggi</font></td>
			</tr>	"""
print """               <tr>
				<td><font color="black" size="3">Luas :</font></td>"""
			
print hitung_luas(sisi=5, alas=4, tinggi=6)
print			"""</tr>"""
print		"""</table>
		</form>
	</body>"""
print "</html>"


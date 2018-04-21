import sys
import subprocess
from subprocess import check_output

class encode:
	
	def __init__(self, file, output):
		rate=self.getRate(file)
		width=self.getWidth(file)
		definition=self.getDefinition(rate, width)
		if definition == "fullthirty" or definition == "hdthirty" or definition == "sdthirty" or definition == "fullsixty" or definition == "hdsixty":
			detel= "--detelecine"
			rate= "23.976"
		if definition == "sdsixty" or definition =="strange":
			detel= "--cfr"
			rate= str(rate)
		if definition == "fullsixty" or definition == "fullthirty":
			width=1280
			quality="21.0"
		if definition == "hdsixty" or definition == "hdthirty":
			width=width
			quality="20.0"
		if definition == "fullthirty" or definition == "hdthirty" or definition == "fullsixty" or definition == "hdsixty":
			subprocess.call(["HandBrakeCLI", "-i", str(file), "--first-subtitle", "-m",  
			"-e", "x264", "-q", str(quality), "-E", "copy", "--audio-fallback", "av_aac", 
			"-w", str(width), "-r", str(rate), str(detel), "--modulus", "16",
			"--h264-level", "4.1", "--x264-preset", "medium", "--x264-tune", "film", "--x264-profile", "auto", 
			"-o", str(output)])
		if definition == "strange" or definition =="sdthirty" or definition =="sdsixty":
			quality="18.0"
			subprocess.call(["HandBrakeCLI", "-i", str(file), "--first-subtitle", "-m",
			"-e", "x264", "-q", str(quality), "-E", "copy", "--audio-fallback", "av_aac",
			"-r", str(rate),  str(detel), "--keep-display-aspect", "--modulus", "16", 
			#"--crop", "<0:0:0:0>",
			"--h264-level", "4.1", "--x264-preset", "medium", "--x264-profile", "auto",
			"-o", str(output)])

	def getRate(self, filename):
		out= subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0",
			"-show_entries", "stream=r_frame_rate", "-of", "default=noprint_wrappers=1:nokey=1",
			str(filename)])
		fps=str(out.decode("utf-8").split('\n')[0])
		rate= fps.split('/')
		rate= str(format(float(rate[0])/float(rate[1]),'.5g'))
		return rate

	def getWidth(self, filename):
		twidth=check_output(["mediainfo", "--Inform=Video;%Width%\\n", str(filename)])
		width=str(twidth.decode("utf-8").strip('\n').split('\n')[0])
		return width

	def getDefinition(self, rate, width):
		if float(rate) == 29.97:
			if int(width) > 1280:
				definition= "fullthirty"
			elif int(width) == 1280:
				definition= "hdthirty"
			elif int(width) < 1280:
				definition= "sdthirty"
		elif float(rate) == 59.94:
			if int(width) > 1280:
				definition= "fullsixty"
			elif int(width) == 1280:
				definition= "hdsixty"
			elif int(width) < 1280:
				definition= "sdsixty"
		else:
			definition="strange"
		print(definition)
		return definition
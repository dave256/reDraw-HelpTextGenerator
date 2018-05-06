# Mark Down to HTML converter for reDraw help documents with Bootstrap stylingimport sysimport redef main(argv):	if len(argv) > 1:		mdToHTML(argv[1])	else:		mdToHTML("Testing/CanvasHelp.md")		def mdToHTML(mdFileName):	# open markdown file	mdFile = open(mdFileName, 'r')	# TODO: generate HTML file	TITLE = ["#", "##"]	LIST = ["*"]	htmlText = []	bootstrapText = []	# Head	htmlText.append(htmlHead())	bootstrapText.append(bootstrapHead())	# Body	introduction = True	tocSectionTitles = []	sections = []	sectionLines = []	htmlSections = []	bootstrapSections = []		htmlFile = open("Testing/CanvasHelp.html", 'w')	for line in mdFile:		words = line.split()		# check if line is blank		if len(words) > 1:			# check if line is a section title			if words[0] in TITLE:     				if len(sectionLines) > 0:					sections.append(sectionLines)				sectionLines = [" ".join(words[1:])]			else:				# add line to section				sectionLines.append(line)	#htmlText.append(htmlBody("\n".join(htmlSections)))	#bootstrapText.append(bootstrapBody("\n".join(bootstrapSections)))	#html = htmlStuff("\n".join(htmlText))	#bootstrap = htmlStuff("\n".join(bootstrapText))	# create file for HTML output	# remove '.md' extension and add '.html'	#htmlFileName = mdFileName[:-3] + ".html"	#writeHTMLFile(html, htmlFileName)	#bootstrapFileName = mdFileName[:-3] + "Bootstrap.html"	#writeHTMLFile(bootstrap, bootstrapFileName)	for s in sections:		for l in s[1:]:			print(parseSectionBody(l, sections), file=htmlFile)	# close files	htmlFile.close()	mdFile.close()def parseSectionBody(line, sections):	line = parseSectionBodyLineForHyperlinks(line, sections)	#line = parseSectionBodyLineForBold(line, sections)	line = parseSectionBodyLineForFormatting(line, "\*\*", "strong")	line = parseSectionBodyLineForFormatting(line, "\*", "i")	line = parseSectionBodyLineForFormatting(line, "\_", "u")	line = parseSectionBodyLineForFormatting(line, "\$", "code")	return linedef parseSectionBodyLineForHyperlinks(line, sections):	matchObj = re.match( r'(.*)\[(.*?)\]\(\#([a-zA-Z0-9-\/]*)\)(.*)', line, re.M|re.I)	if matchObj:		a = findPanelId(matchObj.group(2), sections)		if a:			return matchObj.group(1) + "<a href='" + a + "'>" + matchObj.group(2) + "</a>" + matchObj.group(4)		else:			#return line			return matchObj.group(1) + "<b><i>UNKNOWN LINK[" + matchObj.group(2) + "]</i></b>" + matchObj.group(4)	else:		return line#def parseSectionBodyLineForBold(line, sections):#	matchObj = re.match( r'(.*) \*\*(.*?)\*\* (.*)', line, re.M|re.I)#	if matchObj:#		return matchObj.group(1) + " <strong>" + matchObj.group(2) + "</strong> " + matchObj.group(3)#	else:#		return linedef parseSectionBodyLineForFormatting(line, terminator, tagname):	pattern = r'(.*)' + terminator + '(.*?)' + terminator + '(.*)'	matchObj = re.match(pattern, line, re.M|re.I)	while matchObj:		line = matchObj.group(1) + "<" + tagname + ">" + matchObj.group(2) + "</" + tagname + ">" + matchObj.group(3)		matchObj = re.match(pattern, line, re.M|re.I)	return linedef findPanelId(title, sections):	for i, s in enumerate(sections):		if s[0] == title:			return "panel_" + str(i)def writeHTMLFile(text, fileName):	# open HTML file for writing	htmlFile = open(fileName, 'w')	# write out file	print(text, file=htmlFile)	# close file	htmlFile.close()# Required HTML Stuffdef htmlStuff(contents):	return '<!DOCTYPE html>' + '\n' + '<html lang="en">' + '\n' + contents + '\n' + '</html>'# Headdef htmlHead():	return ""def bootstrapHead():	return ""# Bodydef htmlBody(contents):	return "" + contents + ""def bootstrapBody(contents):	return "" + contents + ""# Sectiondef htmlSection(lines):	text = ""	# Opening tags	# Title of section (lines[0])	# Body of section (lines[1:])	# TODO: Check for formatting characters (like *, ###, etc.)	# Closing tags	return textdef bootstrapSection(lines):	text = ""	# Opening tags	# Title of section (lines[0])	# Body of section (lines[1:])	# TODO: Check for formatting characters (like *, ###, etc.)	# Closing tags	return textif __name__ == '__main__':	main(sys.argv)	
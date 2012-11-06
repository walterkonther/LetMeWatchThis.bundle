from htmlentitydefs import name2codepoint as n2cpimport re# Substitute single HTML entity with match real character.def substitute_entity(match):	ent = match.group(3)		if match.group(1) == "#":		if match.group(2) == '':			return unichr(int(ent))		elif match.group(2) == 'x':			return unichr(int('0x'+ent, 16))	else:		cp = n2cp.get(ent)		if cp:			return unichr(cp)		else:			return match.group()################################################################################ Replace encoded HTML entities with matching real character.def decode_htmlentities(string):	entity_re = re.compile(r'&(#?)(x?)(\d{1,5}|\w{1,8});')	return entity_re.subn(substitute_entity, string)[0]
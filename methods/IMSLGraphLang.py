class GraphLang:
	def __init__(self, ldict=None):
		if ldict is None:
			ldict = {}
		self.ldict = ldict
		self.edge_name = list()
		# update edges between langs
		self.edges()
		self.all_path_trans = []
		self.all_path_pairs = []

	def add_lang(self, lang):
		"""
		Add the lang as a key
		:param: lang: string (2 chars)
		:return:
		"""
		if lang not in self.ldict:
			self.ldict[lang] = []

			for curr_lang in self.ldict:
				if lang == curr_lang:
					continue
				self.add_edge(curr_lang, lang)
				self.add_edge(lang, curr_lang)

	def add_edge(self, lang_a, lang_b):
		"""
		Add the lang as a key
		:param: langA: string (2 chars)
		:param: langB: string (2 chars)
		:return:
		"""

		if lang_a in self.ldict:
			self.ldict[lang_a].append(lang_b)
		else:
			self.ldict[lang_a] = [lang_b]

	def get_langs(self):
		"""
		Get the keys of the dictionary
		:param:
		:return: list of langs
		"""
		return list(self.ldict.keys())

	def edges(self):
		"""
		Ricalcola tutte le possibili transizioni abilitate tra i diversi linguaggi
		modifica
		:param:
		:return: list of possibile translations
		"""
		self.find_edges()
		return self.edge_name

	def find_edges(self):
		"""
		Find the distinct list of edges. set attribute edge_name
		:param:
		:return: list of langs
		"""
		self.edge_name = []
		for langA in self.ldict:
			for langB in self.ldict[langA]:
				# if {langB, langA} not in edge_name: # per collegamenti univoci tra langs
				self.edge_name.append({langA, langB})

	def find_all_path_translation(self, curr_lang, deep):
		self.all_path_trans = self.find_all_paths(curr_lang, deep)
		self.set_lang_pairs()

	def get_all_path_translation(self):
		return self.all_path_trans

	def get_set_lang_pairs(self):
		return self.all_path_pairs

	def find_all_paths(self, curr_lang, deep, path=None):
		"""
		Trova tutti i path di traduzione che partono e arrivano su currLang
		:param: currLang: string lingua corrente
		:param: deep: profondità del path richiesta
		:param: path: sequenza di leng corrente
		:return: list of langs
		"""
		if path is None:
			path = []
		if deep < 3:
			return []
		path = path + [curr_lang]
		# controllo che il path abbia esattamente (-1) gli elementi richiesti
		# -1 perchè d'ufficio aggiungo il nodo iniziale: voglio ritornare alla lingua di origine
		if deep == len(path) + 1:
			# aggiungo nuovamente nodo iniziale per ritornare al lang di partenza
			path.append(path[0])
			return [path]
		if curr_lang not in self.ldict:
			return []
		paths = []
		for lang in self.ldict[curr_lang]:
			# non voglio passare dal nodo iniziale
			if lang == path[0]:
				continue
			new_paths = self.find_all_paths(lang, deep, path)
			for new_path in new_paths:
				paths.append(new_path)
		return paths

	def set_lang_pairs(self):
		self.all_path_pairs = []
		for path in self.all_path_trans:
			path_pair = []
			for i in range(1, len(path)):
				path_pair.append((path[i - 1], path[i]))
			self.all_path_pairs.append(path_pair)
			# os.sys.exit(-1)

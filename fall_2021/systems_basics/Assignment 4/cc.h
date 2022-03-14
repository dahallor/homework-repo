typedef struct CComp CComp;

enum {
	Nmaker = 16,
	Nmodel = 32,
	Ncpu = 8,
	Ndesc = 192,
};

struct CComp {
	int id;
	char maker[Nmaker];
	char model[Nmodel];
	int year;
	char cpu[Ncpu];
	char desc[Ndesc];
};

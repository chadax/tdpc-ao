		PROJET - PYTHON
		_______________
	Buts:
		- Programmer les algorithmes vus en cours sur les listes
		- Manipuler les fichiers (écriture, lecture)
		- Ecriture d'une liste dans un fichier et reconstitution d'une liste à partir d'un fichier
		- Donner quelques astuces permettant d'aborder un mini-PROJET

	Projet:
		ATPC-AO (Analyse des Taux de Participation aux Cours, Assistée par Ordinateur)
		======= 
		le projet ATPC-AO va se clore par la réalisation d'un programme écrit en python 
		qui analysera les taux de participation d'un étudiant a ses cours, sachant que
		si celui-ci	a un TDP <= à 75% dans un cours X, il ne passera l'épreuve
		de ce cours qu'à la seconde session.
		
		Résultats Attendus
		------------------
		ATPC-AO a pour mission, la mise au point de ce programme informatique qui donnera
		entre-autres les résultats suivants:
		
			- la liste complète des tous les étudiants qui auront un TDPC <= 75%
			- la liste des présences d'un étudiant à un cours, connaissant son matricule
					Ex: date1, P|A, leçon (où P = présent et A = absent)
			- jutifier l'absence d'un étudiant connaissant son matricule
			- le TDP d'un étudiant à un cours, connaissant son matricule
			- les TDPs d'un étudiant à tous ses cours, toujours connaissant son matricule
					Ex: N° TDP, Cours, Enseignant


		Données à traiter
		-----------------
		ATPC-AO travaillera sur les données provenant des fichiers excel, càd qu'il faudra
		les importer :
			- etudiants : mat, identite, promotion, date_inscription
			- cours		: acronyme, intitule, promotion, date_debut, enseignant
			- présences	: mat_etud, pres, justify

		Astuces sur l'organisation des fichier et dossier
		-------------------------------------------------
		1. A chaque fois qu'il faudra prélever les présences dans une promotion, il faudra préalablement
		enregistrer la séance c.à.d:
			- seance	: acro_cours, date_seance, [AM|PM], lecon 
							acro_cours	: représente le cours
							date_seance	: représente la date de la séance
							AM|PM 		: indique si la séance est d'avant ou après-midi
							lecon 		: la leçon donnée par l'enseignant
		2. Toutes les présences prélevées à une séance d'un cours dans une promotion seront enregistrées
		dans un fichier nommé avec la date de la séance, suivi d'un '_' puis 'AM' ou 'PM' selon que 
		la séance était d'avant ou apres-midi.
		3. Tous les fichiers de présence d'un cours seront dans un même dossier nommé avec l'acronyme cours
		4. Tous les dossiers de présence seront ensemble dans un même dossier principal nommé presences
		5. Tous les fichiers et dossiers seront regoupés dans un même dossier principal nommé atpc
		
		Vue arborescente des dossiers et fichiers:
		------------------------------------------
			- atpc/etudiants.txt							: tous les étudiants
			- atpc/cours.txt								: tous les cours
			- atpc/seances.txt								: toutes les séances des cours
			- atpc/presences/acro_cours/date_am_pm.txt		: présences regroupé par séance puis cours
	
			
	Modèle:
		- cours		: acronyme, intitule, promotion, date_debut, enseignant
		- seance	: acro_cours, date_seance, [AM|PM], resume
		- etudiant  : mat, identite, promotion, date_inscription
		- presence  : mat_etud, pres, justify

===========================================================================================
===========================================================================================


	---------------------- AMELIORATIONS ATTENDUES ---------------------------
						-----------------------------
	+ Afficher les TDPC d'un étudiant à un ensemble de cours iniqués en paramètre
	+ Considérer un étudiant comme présent si son absence a été justifiée
	+ Afficher uniquement les TDPC des étudiant avec un TDP <= 75%
	+ Créer une commande qui permettra de juistifier une absence


	* Afficher les TDPC dans un histogramme
	* Permettre une jsutification d'absence à distance (en réseau local)
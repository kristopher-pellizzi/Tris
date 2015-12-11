def partita(giocatore1, giocatore2):
	giocatori=[giocatore1, giocatore2]
	N=3
	crea_matrice(N)
	numero_partite=6
	giocatore_iniziale=1
	vittorie=[0,0]
	for x in range(numero_partite):
		vittoria=False
		giocatore=x%2+1
		print("Inizia il giocatore ", giocatore)
		m=crea_matrice(N)
		stampa_matrice(m)
		while not (is_full(m)) and not vittoria:
			i,j=giocatori[giocatore-1](copy.deepcopy(m),giocatore)
			if not 0<=i<N or not 0<=j<N or m[i][j]!=0:
				print("\nIl giocatore ", giocatore, "ha fatto una mossa non valida! SQUALIFICATO!")
				vittoria=inverti_giocatore(giocatore)
			else:
				mossa(m,giocatore,i,j)
				stampa_matrice(m)
				vittoria=check_tris(m)
			giocatore=inverti_giocatore(giocatore)
		if vittoria:
			print("Ha vinto il giocatore ", inverti_giocatore(giocatore))
			vittorie[inverti_giocatore(giocatore)-1]+=1
		else:
			print("pareggio")
		sleep(5)
		print("")

	for i in range(2):
		print("Il giocatore ",i+1," ha vinto ",vittorie[i]," volte")

def stampa_matrice(m):
	print("")
	for riga in m:
		print(riga)
	print("---------")
	sleep(3)

def mossa(m,giocatore,riga,colonna):
	m[riga][colonna]=giocatore

def inverti_giocatore(x):
	return 3-x

def crea_matrice(n):
	return [[0 for _ in range(n)] for _ in range(n)]

def giocatore1(mat,g):
	if num_mosse(mat) in (0,1):
		i=1
		j=1
		if mat[i][j]==0:
			return (i,j)
		else:
			for i in (0,2):
				for j in (0,2):
					if mat[i][j]==0:
						return(i,j)

	if num_mosse(mat)==2:
		if mat[1][1]==g:
			for i in (0,2):
				for j in (0,2):
					if mat[i][j]==0:
						return (i,j)
		else:
			for i in range(3):
				for j in range(3):
					if mat[i][j]==g:
						r=riga(mat,i)
						c=colonna(mat,j)
						break
			if len(set(r))==2:
				return (i,2-j)
			else:
				return (2-i,j)

	if num_mosse(mat) in (3,4,5,6,7):
		if mat[1][1]==g:
			if (len(set(diag_p(mat)))==2 and sorted(diag_p(mat))[0]==0 and num_mosse_terna(diag_p(mat))==2):
				for i in range(3):
					if mat[i][i]==0:
						return (i,i)
			
			if (len(set(diag_s(mat)))==2 and sorted(diag_s(mat))[0]==0 and num_mosse_terna(diag_s(mat))==2):
				for i in range(3):
					if mat[i][2-i]==0:
						return (i,2-i)
		for i in range(3):
			for j in range(3):
				if mat[i][j]==g:
					r=riga(mat,i)
					c=colonna(mat,j)
					if(len(set(r))==2 and sorted(r)[0]==0 and num_mosse_terna(r)==2):
						return (i,blocca(r))
						
					if(len(set(c))==2 and sorted(c)[0]==0 and num_mosse_terna(c)==2):
						return (blocca(c),j)
		if (mat[1][1]!=0 and mat[1][1]!=g):
			if (len(set(diag_p(mat)))==2 and sorted(diag_p(mat))[0]==0 and num_mosse_terna(diag_p(mat))==2):
				for i in range(3):
					if mat[i][i]==0:
						return (i,i)
			
			if (len(set(diag_s(mat)))==2 and sorted(diag_s(mat))[0]==0 and num_mosse_terna(diag_s(mat))==2):
				for i in range(3):
					if mat[i][2-i]==0:
						return (i,2-i)
		for i in range(3):
			for j in range(3):
				if (mat[i][j]!=0 and mat[i][j]!=g):
					r=riga(mat,i)
					c=colonna(mat,j)
					if(len(set(r))==2 and sorted(r)[0]==0 and num_mosse_terna(r)==2):
						return (i,blocca(r))
						
					if(len(set(c))==2 and sorted(c)[0]==0 and num_mosse_terna(c)==2):
						return (blocca(c),j)
		if mat[1][1]==g:
			if (len(set(diag_p(mat)))==2 and sorted(diag_p(mat))[0]==0):
				for i in range(3):
					if mat[i][i]==0:
						return (i,i)
			
			if (len(set(diag_s(mat)))==2 and sorted(diag_s(mat))[0]==0):
				for i in range(3):
					if mat[i][2-i]==0:
						return (i,2-i)
		for i in range(3):
			for j in range(3):
				if mat[i][j]==g:
					r=riga(mat,i)
					c=colonna(mat,j)
					if(len(set(r))==2 and sorted(r)[0]==0):
						return (i,blocca(r))
						
					if(len(set(c))==2 and sorted(c)[0]==0):
						return (blocca(c),j)

	if num_mosse(mat)==8:
		for i in range(3):
			for j in range(3):
				if mat[i][j]==0:
					return(i,j)

def giocatore2(mat,g):
	i=eval(input("Inserisci la prima coordinata (numero di riga da 0 a 2): "))
	j=eval(input("Inserisci la seconda coordinata (numero di colonna da 0 a 2): "))
	return (i,j)

from time import sleep
import copy

def is_full(m):
	c=[m[i][j]==0 for i in range(3) for j in range(3)]
	return 0 if sum(c)>0 else 1

def check_set(lista):
	if len(set(lista))==1:
		return lista[0]
	return False

def check_rows(m):
	for i in range(3):
		if check_set(riga(m,i)):
			return True
	return False

def check_columns(m):
	for i in range(3):
		if check_set(colonna(m,i)):
			return True
	return False

def check_diag(m):
	for i in range(3):
		if (check_set(diag_p(m)) or check_set(diag_s(m))):
			return True
	return False

def check_tris(m):
	return check_rows(m) or check_columns(m) or check_diag(m)

def num_mosse(mat):
	return len([mat[i][j] for i in range(3) for j in range(3) if mat[i][j]!=0])

def num_mosse_terna(terna):
	return len([terna[i] for i in range(3) if terna[i]!=0])

def riga(m,n):
	return [m[n][i] for i in range(3)]

def colonna(m,n):
	return [m[i][n] for i in range(3)]

def diag_p(m):
	return [m[i][i] for i in range(3)]

def diag_s(m):
	return [m[i][2-i] for i in range(3)]

def blocca(tris):
	for i in range(3):
		if tris[i]==0:
			return i

partita(giocatore1,giocatore2)

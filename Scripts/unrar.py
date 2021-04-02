from pyunpack import Archive
import patoolib

def unrar(file_add:str,to_add:str):
	Archive(file_add).extractall(to_add)

if __name__ == "__main__":
	unrar('/Users/siddharthsen/Downloads/Udacity_-_Full_Stack_Web_Developer_Nanodegree_v4.rar','/Users/siddharthsen/Desktop/Udacity')


	

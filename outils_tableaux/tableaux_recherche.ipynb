{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8c9e735d-a45e-422c-a9b8-aa5a585b8b04",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "val dicho : 'a array -> 'a -> bool = <fun>\n"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "text/plain": [
       "val doublons : 'a array -> (int * int) list = <fun>\n"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "ename": "interrupt",
     "evalue": "intterupt",
     "output_type": "error",
     "traceback": [
      "\u001b[31mException: Sys.Break.\u001b[0m"
     ]
    }
   ],
   "source": [
    "(*recherche dans un tableau:*)\n",
    "\n",
    "(*recherche d'un élément dans un tableau trié avec la méthode dichotomique*)\n",
    "let dicho t e =\n",
    "    let rec aux i j =\n",
    "        if i > j then false (*\" cas de base\" *)\n",
    "        else let m = (i + j)/2 in (* on va au milieu *)\n",
    "        if t.(m) = e then true (*on regarde si l'élément du milieu est e*)\n",
    "        else if t.(m) < e then aux (m + 1) j (*Si ce n'est pas le cas, on regarde si l'élément du milieu est plus petit que e et si oui on regarde à droite*)\n",
    "        else aux i (m - 1) (*sinon on se déplace regarde à gauche*)\n",
    "    in aux 0 (Array.length t - 1)\n",
    "    \n",
    "    \n",
    "(*recherche de doublons dans une liste non triée*)\n",
    "let rec doublons t =\n",
    "    let u = Array.length t in\n",
    "        let rec aux i j =  (*on regarde parmis t.(i),...,t.(j)*)\n",
    "            if i = u then [] (* \"cas de base\" *)\n",
    "            else if j = u then aux (i + 1) (i + 2) (*si une fois le tableau scanné on a trouvé aucun élément identique à t.(i), (soit qu'on est à la fin du tableau) alors on passe au prochain élément d'indice i+1*) \n",
    "            else if t.(i) = t.(j) then (i, j)::aux (i + 1) (i + 2) (*si on trouve un élément t.(j) identique à t.(i) alors on ajoute le couple (i, j) à la liste*)\n",
    "            else aux i (j + 1) in (*sinon on passe à l'élément d'indice j+1*)\n",
    "        aux 0 1\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "OCaml default",
   "language": "OCaml",
   "name": "ocaml-jupyter"
  },
  "language_info": {
   "codemirror_mode": "text/x-ocaml",
   "file_extension": ".ml",
   "mimetype": "text/x-ocaml",
   "name": "OCaml",
   "nbconverter_exporter": null,
   "pygments_lexer": "OCaml",
   "version": "4.08.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

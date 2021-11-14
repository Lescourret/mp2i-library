(*fusionner deux listes*)


let rec fusion l1 l2 = match l1, l2 with
| [], _ -> l2 (*cas de base*)
| _, [] -> l1 (*cas de base*)
| e1::q1, e2::q2 when e1 < e2 -> e1::fusion q1 l2 (*tous les éléments de la liste l1 fusionné dans la liste finale*)
| e1::q1, e2::q2 -> e2::fusion l1 q2 (*puis, tous les éléments de l2*)

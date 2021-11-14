(*fusionner deux listes triées*)


let rec fusion l1 l2 = match l1, l2 with
| [], _ -> l2 (*cas de base*)
| _, [] -> l1 (*cas de base*)
| e1::q1, e2::q2 when e1 < e2 -> e1::fusion q1 l2 (* Si l'élément e1 est plus petit que e2 alors il est fusionné à la liste finale*)
| e1::q1, e2::q2 -> e2::fusion l1 q2 (*sinon, c'est l'élément e2 *)

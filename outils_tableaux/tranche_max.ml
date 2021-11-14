(*recherche de la tranche maximale d'un tableau avec l'algorithme de Kadane*)


let tranche_max t =
    let s = ref t.(0) in (*déf d'une référence s*)
    let sj = ref t.(0) in (*déf d'une référence sj*)
        for j = 1 to Array.length t - 1 do (*boucle for*)
            sj := max (!sj + t.(j)) t.(j); (*definition de la somme sj = max(sj−1 + t.(j), t.(j))*)
            s := max !s !sj (*on conserve la plus grande des deux sommes*)
        done;
    !s;;

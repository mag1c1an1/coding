use std::vec;

struct Solution;
impl Solution {
    pub fn maximum_detonation(bombs: Vec<Vec<i32>>) -> i32 {
        let n = bombs.len();
        let can_boom = |u: usize, v: usize| -> bool {
            let dx = (bombs[u][0] - bombs[v][0]) as i64;
            let dy = (bombs[u][1] - bombs[v][1]) as i64;
            (bombs[u][2] as i64).pow(2) >= dx.pow(2) + dy.pow(2)
        };
        let mut g = vec![vec![]; n];
        for i in 0..n {
            for j in 0..n {
                if i != j && can_boom(i, j) {
                    g[i].push(j);
                }
            }
        }
        let mut res = 0;
        for i in 0..n {
            let mut visited = vec![false; n];
            res = res.max(dfs(&g, i, &mut visited));
        }
        res
    }
}

fn dfs(g: &Vec<Vec<usize>>, start: usize, visited: &mut Vec<bool>) -> i32 {
    let mut cnt = 1;
    visited[start] = true;
    for &i in g[start].iter() {
        if !visited[i] {
            cnt += dfs(g, i, visited);
        }
    }
    cnt
}

fn main() {
    // let bombs = vec![
    //     vec![1, 2, 3],
    //     vec![2, 3, 1],
    //     vec![3, 4, 2],
    //     vec![4, 5, 3],
    //     vec![5, 6, 4],
    // ];
    let bombs = vec![vec![1, 1, 5], vec![10, 10, 5]];
    let ans = Solution::maximum_detonation(bombs);
    println!("{ans}");
}

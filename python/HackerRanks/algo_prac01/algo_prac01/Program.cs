using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace algo_prac01
{
    class Program
    {
        static int[] climbingLeaderboard(int[] scores, int[] alice)
        {
            int[] rank = new int[alice.Length];
            List<int> ranking = new List<int>();
            List<int> steps = new List<int>(scores);
            int i = 0;
            steps = steps.Distinct().ToList();
            foreach(int num in steps)
            {
                Console.WriteLine(num);
            }
            foreach (int num in alice)
            {
                for (int j = 0; j < steps.Count; j++)
                {
                    if (num >= steps[j])
                    {
                        rank[i] = j + 1;
                        break;
                    }                    
                }
                if (rank[i] == 0)
                {
                    rank[i] = steps.Count+1;
                }
                i++;
            }
            return rank;
        }

        static void Main(string[] args)
        {
            int[] scores = { 100, 100, 50, 40, 40, 20, 10 };
            int[] alice = { 5, 25, 50, 120 };
            int[] rank = climbingLeaderboard(scores, alice);
            Console.WriteLine();
            foreach (int num in rank)
            {
                Console.WriteLine(num);
            }
        }
    }
}

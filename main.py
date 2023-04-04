import labyrinthpy.Labyrinth_generation.DFS_generation
import labyrinthpy.Labyrinth_generation.MST_Prims_generation
import labyrinthpy.Labyrinth_generation.MST_Kruskals_generation

#m = labyrinthpy.Labyrinth_generation.DFS_generation.generate_dfs(30, 10)

m = labyrinthpy.Labyrinth_generation.MST_Prims_generation.generate_mst_prims(30, 30)

m.visualize()
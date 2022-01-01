class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        from queue import Queue
        dir_list = [(-1, 0),
                   (1, 0), 
                   (0, 1), 
                   (0, -1)
                   ]
        
        q = Queue()
        q.put((sr, sc))
        visited = set()
        
        # print(image[sr][sc])
        while not q.empty():
            _rw, _cl = q.get()
            print(_rw, _cl)
            visited.add((_rw, _cl))
            for r, c in dir_list:
                    rw, cl = r + _rw, c + _cl
                    print(rw, cl, visited)
                    if ((rw in range(len(image)))
                    and (cl in range(len(image[0])))
                    and (image[rw][cl] == image[sr][sc])
                    and ((rw, cl) not in visited)):
                        print(rw, cl)
                        image[rw][cl] = newColor
                        visited.add((rw, cl))
                        q.put((rw, cl))
        image[sr][sc] = newColor
        return image

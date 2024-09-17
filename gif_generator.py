import chess
import io
import cairosvg
import chess.pgn
import imageio
from PIL import Image

class ChessGifGenerator:
    def __init__(self):
        self.board = chess.Board()
    
    def draw_board(self, board):
        
        svg_code = chess.svg.board(board)
        png_data = cairosvg.svg2png(bytestring=svg_code.encode('utf-8'))
        return Image.open(io.BytesIO(png_data))
    
    def create_gif(self, pgn_string, gif_path):
        node = chess.pgn.read_game(io.StringIO(pgn_string))
        frames = []
        while node.variations:
            next_node = node.variation(0)
            board = next_node.board()
            img = self.draw_board(board)
            frames.append(img)
            node = next_node
        
        # last board state
        frames.append(self.draw_board(node.board()))
        
        # Save gif
        imageio.mimsave(gif_path, frames, duration=1)

if __name__ == "__main__":
    
    s = '1. d3 e6 2. Nd2 Be7 3. Ngf3 d5 4. g3 Nf6 5. Bg2 O-O 6. O-O c5 7. Re1 d4 8. e4 dxe3 9. fxe3 Nc6 10. e4 Qc7 11. c3 Nd7 12. Qc2 e5 13. Nf1 f6 14. Ne3 a6 15. Nd5 Qd6 16. Be3 f5 17. exf5 Qxd5 18. Nd4 Qf7 19. Ne6 Nf6 20. Nxf8 Bxf8 21. d4 cxd4 22. cxd4 exd4 23. Bf4 g6 24. fxg6 Qxg6 25. Qc4+ Kg7 26. Rf1 Bf5 27. Rae1 Be4 28. Bxe4 Nxe4 29. Qd5 Bc5 30. Qxe4 d3+ 31. Kg2 Qxe4+ 32. Rxe4 Rf8 33. Rd1 Nb4 34. Rxb4 Bxb4 35. Rxd3 Bd6 36. Rf3 Bxf4 37. Rxf4 Re8 38. Rf3 Re2+ 0-1'

    gif_generator = ChessGifGenerator()
    gif_generator.create_gif(pgn_string=s, gif_path='chess_game.gif')
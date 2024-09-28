from gif_generator import ChessGifGenerator
from chess_data import ChessData


if __name__ == "__main__":
    
    chess_data = ChessData()
    
    f = "Alexander-Alekhine_vs_Lupi-Francesco_1946.pgn"
    
    info, moves = chess_data.run(f)
    
    print(info)
    
    gif_generator = ChessGifGenerator()
    gif_generator.create_gif(pgn_string=moves, gif_path='chess_game.gif')
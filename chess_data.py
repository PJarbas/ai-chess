import chess.pgn


class ChessData:
        
    def read_game(self, pgn_file):
        
        with open(pgn_file) as f:
            game = chess.pgn.read_game(f)
        return game
    
    def get_moves(self, game):
        return str(game.mainline())
        
    def get_result(self, result):
        
        if not result:
            return None
        
        res_dict = {
            '1-0': 'White wins',
            '0-1': 'Black Wins',
            '1/2-1/2': 'Draw'
        }
        
        return res_dict[result]
    
    def extract_header(self, game):
        white_player = game.headers["White"]
        black_player = game.headers["Black"]
        
        site = game.headers["Site"]
        _date = game.headers["Date"]
        
        event = game.headers["Event"]
        result = self.get_result(game.headers["Result"])
        
        return white_player, black_player, site, _date, event, result
        
        
    def get_chess_match_info(self, game):
        
        white_player, black_player, site, _date, event, result = self.extract_header(game)
        
        text = f"{white_player} vs {black_player}\n{event} - {site} - {_date}\nResult: {result}"
        
        return text
    
    def run(self, pgn_file):
        game = self.read_game(pgn_file)
        
        moves = self.get_moves(game)
        
        match_info = self.get_chess_match_info(game)
        
        return match_info, moves     


if __name__ == '__main__':
    chess_data = ChessData()
    f = "Alexander-Alekhine_vs_Lupi-Francesco_1946.pgn"
    info, m = chess_data.run(f)
    print(info)
    print(m)
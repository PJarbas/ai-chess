import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# https://betterdatascience.com/send-emails-with-python/

class ChessEmailSender:
    def __init__(self, smtp_server, smtp_port, smtp_user, smtp_password, from_email, to_email, gif_path):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password
        self.from_email = from_email
        self.to_email = to_email
        self.gif_path = gif_path
        self.msg = MIMEMultipart('related')

    def setup_email(self, subject, chess_match_info, chess_moves):
        self.msg['From'] = self.from_email
        self.msg['To'] = self.to_email
        self.msg['Subject'] = subject

        html = f"""
        <html>
        <head>
        <style>
            body {{ font-family: Arial, sans-serif; }}
            .chess-info {{ margin-bottom: 20px; }}
            .chess-moves {{ white-space: pre-wrap; }}
        </style>
        </head>
        <body>
            <div class="chess-info">
                <h2>{subject}</h2>
                <pre>{chess_match_info}</pre>
            </div>
            <div class="chess-moves">
                <p>{chess_moves}</p>
            </div>
            <img src="cid:chess_game_gif" alt="Partida de Xadrez">
        </body>
        </html>
        """

        self.msg.attach(MIMEText(html, 'html'))

    def attach_gif(self):
        with open(self.gif_path, 'rb') as gif:
            msg_image = MIMEImage(gif.read())
            msg_image.add_header('Content-ID', '<chess_game_gif>')
            self.msg.attach(msg_image)

    def send_email(self):
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.smtp_user, self.smtp_password)
            server.sendmail(self.from_email, self.to_email, self.msg.as_string())
        print('E-mail enviado com sucesso!')

# Exemplo de uso
if __name__ == '__main__':
    sender = ChessEmailSender(
        smtp_server='smtp.example.com',
        smtp_port=587,
        smtp_user='your-email@example.com',
        smtp_password='your-password',
        from_email='your-email@example.com',
        to_email='recipient@example.com',
        gif_path='chess_game.gif'
    )

    chess_match_info = """
    [Event "F/S Return Match"]
    [Site "Belgrade, Serbia JUG"]
    [Date "1992.11.04"]
    [Round "29"]
    [White "Fischer, Robert J."]
    [Black "Spassky, Boris V."]
    [Result "1/2-1/2"]
    """

    chess_moves = """
    1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 d6 8. c3
    O-O 9. h3 Nb8 10. d4 Nbd7 11. c4 c6 12. cxb5 axb5 13. Nc3 Bb7 14. Bg5 h6 15.
    Bh4 Nh7 16. Bxe7 Qxe7 17. a3 Kh8 18. Qd3 f5 19. exf5 Ndf6 20. Nh4 Qe8 21. Ng6+
    Kg8 22. Nxf8 Kxf8 23. g4 Ng5 24. Kg2 c5+ 25. f3 c4 26. Qd1 e4 27. fxe4 Nfxe4
    28. Nxe4 Bxe4+ 29. Kg3 Qe5+ 30. Kh4 Nf3+ 31. Kh5 Qh2 32. h4 Qg3 33. Rh1 Qf2
    34. Qf1 Qxf1 35. Rhxf1 Ke7 36. g5 hxg5 37. hxg5 Rh8+ 38. Kg4 Ne5+ 39. Kg3 Rf8
    40. Rae1 d5 41. Rf4 Kd6 42. Ref1 Rxf4 43. Rxf4 Nd3 44. Rf8 Nxb2 45. Rb8 Kc5
    46. Rxb7 Nd3 47. g6 Ne5 48. g7 d4 49. g8=Q d3 50. Qc8+ Kd4 51. Rd7+ Ke3 52.
    Qe8 d2 53. Qxe5# 1-0
    """

    subject = "Partida de Xadrez: Fischer vs Spassky"
    sender.setup_email(subject, chess_match_info, chess_moves)
    sender.attach_gif()
    sender.send_email()

import numpy as np


def make_board(board_string):
    brett = []
    liste = list(board_string)
    plass = -1
    for i in liste:
        plass += 1
        if i == ".":
            liste[plass] = " "
    for i in range(0, 8):
        rad = []
        for j in range((i * 8), (i * 8) + 8):
            rad.append(liste[j])
        brett.append(rad)
    return brett


def make_board1(board_string):
    liste = list(board_string)
    plass = -1
    for i in liste:
        plass += 1
        if i == ".":
            liste[plass] = " "
    liste = np.array(liste)
    liste = liste.reshape(8, 8)
    return liste


def get_piece(board, x, y):
    brett = board
    kolonne = brett[8 - (y)]
    tall = kolonne[x - 1]
    return tall


def motstander_brikke(index):
    if index == 1:
        brikk = "♟♜♞♝♚♛♝♞♜"
    else:
        brikk = "♖♘♗♕♔♗♘♖♙"
    return brikk


def lovlig_trekk_bonde(board, x, y):
    if x >= 9 or y >= 9:
        return "Dette er utfor sjakkbrettet"
    brikke = get_piece(board, x, y)
    mulige_trekk = []
    if brikke in "♖♘♗♕♔♗♘♖♙":
        farge = 1
    elif brikke in "♟♜♞♝♚♛♝♞♜":
        farge = -1
    else:
        farge = 0
    motstander = motstander_brikke(farge)
    for i in range(8):
        if brikke == "♟" or brikke == "♙":
            if board[-y + 8] == board[i]:
                if brikke in board[i]:
                    if brikke in board[0] or brikke in board[-1]:
                        return []
                    else:
                        if x < 8:
                            if board[i - farge][x - 1] == " ":
                                mulige_trekk.append((x, y + farge))
                            if board[i - farge][x - 1] == " " and board[i - (2 * farge)][x - 1] == " ":
                                mulige_trekk.append((x, y + 2 * farge))
                            if board[i - farge][x - 2] in motstander:
                                mulige_trekk.append((x - 1, y + farge))
                            if board[i - farge][x] in motstander:
                                mulige_trekk.append((x + 1, y + farge))
                            return mulige_trekk
                        else:
                            if board[i - farge][x - 1] == " ":
                                mulige_trekk.append((x, y + farge))
                            if board[i - farge][x - 1] == " " and board[i - (2 * farge)][x - 1] == " ":
                                mulige_trekk.append((x, y + 2 * farge))
                            if board[i - farge][x - 2] in motstander:
                                mulige_trekk.append((x - 1, y + farge))
                            return mulige_trekk

        else:
            return []


def lovlig_trekk_hest(board, x, y):
    if x >= 9 or y >= 9:
        return "Dette er utfor sjakkbrettet"
    brikke = get_piece(board, x, y)
    mulige_trekk = []
    if brikke in "♖♘♗♕♔♗♘♖♙":
        farge = 1
    elif brikke in "♟♜♞♝♚♛♝♞♜":
        farge = -1
    else:
        farge = 0
    motstander = motstander_brikke(farge)

    for i in range(8):
        if brikke == "♞" or brikke == "♘":
            if board[-y + 8] == board[i]:
                if brikke in board[i]:
                    if brikke in board[0][x - 1] or brikke in board[-1][x - 1]:
                        if x == 8:
                            if board[i - (2 * farge)][x - 2] == " " or board[i - (2 * farge)][x - 2] in motstander:
                                mulige_trekk.append((x - 1, y + (2 * farge)))
                            if board[i - farge][x - 3] == " " or board[i - farge][x - 3] in motstander:
                                mulige_trekk.append((x - 2, y + farge))
                            return mulige_trekk
                        if x == 7:
                            if board[i - (2 * farge)][x - 2] == " " or board[i - (2 * farge)][x - 2] in motstander:
                                mulige_trekk.append((x - 1, y + (2 * farge)))
                            if board[i - farge][x - 3] == " " or board[i - farge][x - 3] in motstander:
                                mulige_trekk.append((x - 2, y + farge))
                            if board[i - (2 * farge)][x] == " " or board[i - (2 * farge)][x] in motstander:
                                mulige_trekk.append((x + 1, y + (2 * farge)))
                            return mulige_trekk
                        else:
                            if board[i - (2 * farge)][x - 2] == " " or board[i - (2 * farge)][x - 2] in motstander:
                                mulige_trekk.append((x - 1, y + (2 * farge)))
                            if board[i - farge][x - 3] == " " or board[i - farge][x - 3] in motstander:
                                mulige_trekk.append((x - 2, y + farge))
                            if board[i - (2 * farge)][x] == " " or board[i - (2 * farge)][x] in motstander:
                                mulige_trekk.append((x + 1, y + (2 * farge)))
                            if board[i - farge][x + 1] == " " or board[i - farge][x + 1] in motstander:
                                mulige_trekk.append((x + 2, y + farge))
                            return mulige_trekk
                    else:
                        if x == 8:
                            if board[i - (2 * farge)][x - 2] == " " or board[i - (2 * farge)][x - 2] in motstander:
                                mulige_trekk.append((x - 1, y + (2 * farge)))
                            if board[i - farge][x - 3] == " " or board[i - farge][x - 3] in motstander:
                                mulige_trekk.append((x - 2, y + farge))
                            if board[i + (2 * farge)][x - 2] == " " or board[i + (2 * farge)][x - 2] in motstander:
                                mulige_trekk.append((x - 1, y - (2 * farge)))
                            if board[i + farge][x - 3] == " " or board[i + farge][x - 3] in motstander:
                                mulige_trekk.append((x - 2, y - farge))
                            return mulige_trekk
                        if x == 7:
                            if board[i - (2 * farge)][x - 2] == " " or board[i - (2 * farge)][x - 2] in motstander:
                                mulige_trekk.append((x - 1, y + (2 * farge)))
                            if board[i - farge][x - 3] == " " or board[i - farge][x - 3] in motstander:
                                mulige_trekk.append((x - 2, y + farge))
                            if board[i - (2 * farge)][x] == " " or board[i - (2 * farge)][x] in motstander:
                                mulige_trekk.append((x + 1, y + (2 * farge)))
                            if board[i + (2 * farge)][x - 2] == " " or board[i + (2 * farge)][x - 2] in motstander:
                                mulige_trekk.append((x - 1, y - (2 * farge)))
                            if board[i + farge][x - 3] == " " or board[i + farge][x - 3] in motstander:
                                mulige_trekk.append((x - 2, y - farge))
                            if board[i + (2 * farge)][x] == " " or board[i + (2 * farge)][x] in motstander:
                                mulige_trekk.append((x + 1, y - (2 * farge)))
                            return mulige_trekk
                        else:
                            if board[i - (2 * farge)][x - 2] == " " or board[i - (2 * farge)][x - 2] in motstander:
                                mulige_trekk.append((x - 1, y + (2 * farge)))
                            if board[i - farge][x - 3] == " " or board[i - farge][x - 3] in motstander:
                                mulige_trekk.append((x - 2, y + farge))
                            if board[i - (2 * farge)][x] == " " or board[i - (2 * farge)][x] in motstander:
                                mulige_trekk.append((x + 1, y + (2 * farge)))
                            if board[i - farge][x + 1] == " " or board[i - farge][x + 1] in motstander:
                                mulige_trekk.append((x + 2, y + farge))
                            if board[i + (2 * farge)][x - 2] == " " or board[i + (2 * farge)][x - 2] in motstander:
                                mulige_trekk.append((x - 1, y - (2 * farge)))
                            if board[i + farge][x - 3] == " " or board[i + farge][x - 3] in motstander:
                                mulige_trekk.append((x - 2, y - farge))
                            if board[i + (2 * farge)][x] == " " or board[i + (2 * farge)][x] in motstander:
                                mulige_trekk.append((x + 1, y - (2 * farge)))
                            if board[i + farge][x + 1] == " " or board[i + farge][x + 1] in motstander:
                                mulige_trekk.append((x + 2, y - farge))
                            return mulige_trekk


        else:
            return []


board = make_board(("♜♞♝♛♚♝♞♜♟♟♟♟♟♟♟♟................................♙♙♙♙♙♙♙♙♖♘♗♔♕♗♘♖"))

package com.company.AlphaChess.board;

import com.company.AlphaChess.common.File;
import com.company.AlphaChess.common.Location;
import com.company.AlphaChess.squares.Square;
import com.company.AlphaChess.squares.SquareColor;

public class Board {
    private static final Integer BOARD_LENGTH = 8; // To assign proper ranks
    Square[][] boardSquares = new Square[8][8];

    public Board(){
        // inverted colors
        for (int i = 0; i<boardSquares.length;i++){
            int col = 0;
            SquareColor currColor = (i % 2 == 0)? SquareColor.LIGHT : SquareColor.DARK;
            for (File file : File.values()){
                Square newSq = new Square(currColor, new Location(file,BOARD_LENGTH - i-1),false);
                boardSquares[i][col] = newSq;
                currColor = (currColor == SquareColor.DARK) ? SquareColor.LIGHT: SquareColor.DARK;
                col++;
            }
        }
    }

    public void printBoard(){
        for (Square[] row: boardSquares){
            for (Square square:row){
                System.out.println(square);
            }
            System.out.println();
        }
    }
}

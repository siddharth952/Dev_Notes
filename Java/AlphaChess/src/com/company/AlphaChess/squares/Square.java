package com.company.AlphaChess.squares;

import com.company.AlphaChess.common.Location;

public class Square {
    private final SquareColor squareColor;
    private final Location location;
    private boolean isOccupied;


    public Square(SquareColor squareColor, Location location, boolean isOccupied) {
        this.squareColor = squareColor;
        this.location = location;
        this.isOccupied = isOccupied;
    }

    public void reset() {
        this.isOccupied = false;
    }

    public SquareColor getSquareColor() {
        return squareColor;
    }

    public Location getLocation() {
        return location;
    }

    public boolean isOccupied() {
        return isOccupied;
    }

    public void setOccupied(boolean occupied) {
        isOccupied = occupied;
    }

    @Override
    public String toString() {
        return "Square{" +
                "squareColor=" + squareColor +
                ", location=" + location +
                ", isOccupied=" + isOccupied +
                '}';
    }
}

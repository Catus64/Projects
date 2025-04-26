
/**
    @author Wan Abdul Rahman
    Implementation of the Tile Piece
 */
public class Tile extends Piece
{
    public Tile(int x,int y)
    {
        super.type = "Tile";
        super.is_alive = false;
        super.posX = x;
        super.posY = y;
        team = "null";
    }

    @Override
    public void pieceMovement(BoardLogicModel BML)
    {
        System.out.println("Tile turns green");
        team = "green";
    
    
    }
}

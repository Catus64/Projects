
/**
 *
 * @author 
 *         Wan Abdul Rahman
 * Observe for invalid inputs
 */
public class pieceObserver
{
    boolean selected;
    int turnCount;
    String turn;
    int currentX,currentY;
    public pieceObserver()
    {
        selected = false;
        turn = "blue";
        currentX = -1;
        currentY = -1;
        turnCount = 1;
    }
    public void toggle()
    {
        selected ^= true;
    }
    public boolean isLock()
    {
        if(selected == true)
        {
            return true;
        }
        else{return false;}
    }
    public void setLock(int x,int y)
    {
        currentX = x;
        currentY = y;
    }
    public boolean checkLock(int x,int y)
    {
        if(currentX == x && currentY == y)
        {
            unlock();
            return true;
        }else{return false;}
    }
    public boolean teamcheck(Piece p)
    {
        System.out.println(p.team);
        System.out.println(turn);
        if(p.team == turn){
            return true;
        }else{
            return false;
        }
    
    
    }
    public void switchTeam()
    {
        if(turn == "blue")
        {
            turn = "red";
        }else{
            turn = "blue";
            turnCount++;
        }
    }
    public void unlock()
    {
        toggle();
        currentX = -1;
        currentY = -1;
    }
}

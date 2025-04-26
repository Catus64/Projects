import javax.swing.JPanel;
import java.awt.*;
import javax.swing.*;
import javax.swing.JLabel;

/**
 * Write a description of class BoardView here.
 *
 * @author Agilan a/l Khali Thasan
 * This is the Board view it acts a component of view. this will handle a panel for the pieces
 * positions and if they are alive/dead/move to a new tile
 * 
 */
public class BoardView extends JPanel
{
    boolean black,switched;
    JButton[][] keys;
    String tempType;
    boolean flip;
    //JLabel Turn;
    
    public BoardView(Controller cntrl,BoardLogicModel BML,View view)
    {
        black = false;
        switched = false;
        this.setBounds(50,50,500,700);
        this.setBackground(Color.red);
        this.setLayout(new GridLayout(8,5));
        keys = new JButton[8][5];
        flip = false;
        for(int i = 0;i<8;i++){
            //setting up the initial board with tiles
            for(int j = 0; j <5; j++){
            int tempy=i;
            int tempx=j;
            JButton temp = new JButton();
            
            if(black){
                temp.setBackground(Color.lightGray);
            }else{
                temp.setBackground(Color.white);
            }
            black ^= true;
            temp.setFocusable(false);
            temp.addActionListener(e -> cntrl.select(tempx,tempy,this,BML,view));
            keys[i][j] = temp;
            this.add(keys[i][j]);
            }
        }
        }
        
    public void initialize(BoardLogicModel BML){
        //initializing the piece based of boardlogicmodel's content
        for(int i = 0;i<8;i++)
        {
            for(int j = 0;j<5;j++){
                if(BML.getPieceType(j,i).equals("Tile"))
                {System.out.println(" Tile ");
                 tempType = "Tile";
                }
                else{
                tempType = BML.getPieceType(j,i);
                setPiece(j,i,tempType,BML.getTeam(j,i));
                }
            }
        }
    }
    
    public void loadGameView(BoardLogicModel BML){
        //initializing the piece based of load function
        for(int i = 0;i<8;i++)
        {
            for(int j = 0;j<5;j++){
                if(BML.getPieceType(j,i).equals("Tile"))
                {System.out.println(" Tile ");
                 tempType = "Tile";
                }
                else{
                tempType = BML.getPieceType(j,i);
                setPiece(j,i,tempType,BML.getTeam(j,i));
                }
            }
        }
    }
    
    public void setPiece(int x,int y,String type,String team)
    {   
        //setting a piece onto a button
        ImageIcon temp = getImage(type,team);
        keys[y][x].setIcon(temp);
    
    }

    private ImageIcon getImage(String type,String team){
        //choosing an image for a piece
        ImageIcon icon;
        if(type == "Ram"){
            if(team.equals("blue")){
            System.out.println("Blue Ram");
            icon = new ImageIcon("Images/b_ram_up.png");
            return icon;
            }
            else{
            System.out.println("Red Ram");
            icon = new ImageIcon("Images/r_ram_down.png");
            return icon;
            }
        }else if(type.equals("Xor")){
            if(team.equals("blue")){
            System.out.println("Blue Xor");
            icon = new ImageIcon("Images/b_xor.png");
            return icon;
            }
            else{
            System.out.println("Red Xor");
            icon = new ImageIcon("Images/r_xor.png");
            return icon;
            }
        }else if(type == "Tor"){
            if(team.equals("blue")){
            System.out.println("Blue Tor");
            icon = new ImageIcon("Images/b_tor.png");
            return icon;
            }
            else{
            System.out.println("Red Tor");
            icon = new ImageIcon("Images/r_tor.png");
            return icon;
            }
        }else if(type == "Biz"){
            if(team.equals("blue")){
            System.out.println("Blue Biz");
            icon = new ImageIcon("Images/b_biz.png");
            return icon;
            }
            else{
            System.out.println("Red Biz");
            icon = new ImageIcon("Images/r_biz.png");
            return icon;
            }
        }else if(type == "Sau"){
            if(team.equals("blue")){
            System.out.println("Blue Sau");
            icon = new ImageIcon("Images/b_sau.png");
            return icon;
            }
            else{
            System.out.println("Red Sau");
            icon = new ImageIcon("Images/r_sau.png");
            return icon;
            }
        }
        icon = new ImageIcon("Images/nothing.png");
        return icon;
    }
    
    public void flipBoard(BoardLogicModel BML)
    {
        //flipping the board by reversing keys x and y numbers
        flip ^= true;
        boolean flips = false;
        for(int i = 0;i<8;i++){
            for(int j = 0; j <5; j++){
            this.remove(keys[i][j]);        
            }
        }
        if(flip == true){
        for(int i = 7;i != -1;i--){
            for(int j = 4; j != -1; j--){
            this.add(keys[i][j]);
                }
            }
        }else{
        for(int i = 0;i < 8;i++){
            for(int j = 0; j < 5; j++){
            this.add(keys[i][j]); 
                }
            }
        }
        for(int i = 0;i<8;i++){
            for(int j=0;j<5; j++){
                if(BML.pieces[i][j].type == "Ram")
                {   
                    flips = flip ^ BML.pieces[i][j].flip;
                    if(BML.pieces[i][j].team == "blue")
                    {
                        if(flips){
                        ImageIcon icon = new ImageIcon("Images/b_ram_down.png");
                        keys[i][j].setIcon(icon);
                        }
                        else{
                        ImageIcon icon = new ImageIcon("Images/b_ram_up.png");
                        keys[i][j].setIcon(icon);
                        }
                    }else
                    {
                        if(flips){
                        ImageIcon icon = new ImageIcon("Images/r_ram_up.png");
                        keys[i][j].setIcon(icon);
                        }else{
                        ImageIcon icon = new ImageIcon("Images/r_ram_down.png");
                        keys[i][j].setIcon(icon);
                        }
                    }
                    //keys[i][j].setIcon();
                }
            }
        }
    }
    
    public void setTileGreen(int x,int y)//setting a tile green(movoable)
    {
        keys[y][x].setBackground(Color.green);
    }
    public void setTileRed(int x,int y)//setting a tile red(killable)
    {
        keys[y][x].setBackground(Color.red);
    }
    public void setTileYellow(int x,int y)//setting a tile yellow(selected)
    {
        keys[y][x].setBackground(Color.yellow);
    }
    public void resetTile(int x, int y)//reset to an empty tile
    {
       int calc = (x + y)%2;
       if(calc != 0){
        keys[y][x].setBackground(Color.lightGray);
        keys[y][x].setIcon(null);
       }else
       {
        keys[y][x].setBackground(Color.white);
        keys[y][x].setIcon(null);
       }
    
    }
    public void clearTarget(int x, int y)//reset to an empty tile after deselecting
    {
       int calc = (x + y)%2;
       if(calc != 0){
        keys[y][x].setBackground(Color.lightGray);
       }else
       {
        keys[y][x].setBackground(Color.white);
       }
    
    }
}

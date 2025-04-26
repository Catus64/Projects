import javax.swing.JFrame;
import java.awt.GridLayout;
import javax.swing.JLabel;
import javax.swing.JPanel;
import java.awt.*;
import javax.swing.*;
import javax.swing.JButton;

/**
 * @author Agilan a/l Khali Thasan
 *         Wan Abdul Rahman
 */
public class Main
{
    

    public static void main(String args[])
    {
        BoardLogicModel BML = new BoardLogicModel();
        Controller controller = new Controller();
        View view = new View(controller,BML);
        
         
        view.Mainmenu(); 
        //view.gameBoard();
        //view.boardView.initialize(BML);
        
        //InitPage page = new InitPage();
        
        /*Controller cntrl = new Controller();
        
        JFrame test = new JFrame();
        test.setSize(1000,1000);
        test.setLayout(null);
        JPanel board = new JPanel();
        board.setBounds(100,50,500,700);
        board.setBackground(Color.red);
        board.setLayout(new GridLayout(8,5));
        int keynum = 1;
        boolean black = false;
        JButton[][] keys = new JButton[8][5];
        test.setVisible(true);
        test.add(board);
        for(int i = 0 ; i < 8 ; i++){
            for(int j = 0; j < 5; j++){
                int tempx=i;
                int tempy=j;
                JButton temp = new JButton();
                
                if(black){
                    temp.setBackground(Color.lightGray);
                }else{
                    temp.setBackground(Color.white);}
                black ^= true;
                temp.setFocusable(false);
                temp.addActionListener(e -> cntrl.select(tempx,tempy));
                keynum++;
                keys[i][j] = temp;
                board.add(keys[i][j]);
            }
        }
        ImageIcon ram = new ImageIcon("Ram.png");
        keys[6][2].setIcon(ram);
    }*/
        }
}

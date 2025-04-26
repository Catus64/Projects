import javax.swing.JFrame;
import javax.swing.ImageIcon;
import javax.swing.JOptionPane;

/**
 * This is the view model
 *
 * @author (Wan Abdul Rahman)
 * The initial JFrame for all other panels.
 */
public class View extends JFrame
{
    MainView mainView;
    BoardView boardView;
    BoardSettings boardSettings;
    
    public View(Controller cntrl,BoardLogicModel BML)
    {
        super.setSize(1000,800);
        super.setLayout(null);
        super.setVisible(true);
        super.setTitle("Kwazam Chess");
        boardView = new BoardView(cntrl,BML,this);
        mainView = new MainView(cntrl,BML,this);
        boardSettings = new BoardSettings(cntrl,BML,this);
    }
    public void gameBoard()
    {
        super.add(boardView);
        super.repaint();
        super.revalidate();
    }
    public void Mainmenu()
    {
        super.add(mainView);
    }
    public void NoMenu()
    {
        mainView.clear();
        super.remove(mainView);
        super.repaint();
    }
    public void BoardSetting()
    {
        super.add(boardSettings);
    }
    /*
    public void removeGameBoard()
    {
        super.remove(boardView);
        //super.revalidate();
    }*/
    public void winNotif(String team)
    {
        if(team == "red"){
        JOptionPane.showMessageDialog(null, "Game ends,"+" blue "+" Win");
        }else{JOptionPane.showMessageDialog(null, "Game ends,"+team+" Win");}
        System.exit(0);
        //boardView.removeBV();
        //removeGameBoard();
        //Mainmenu();
        //mainView.rePopulate();
    }
    public void instruction()
    {
        JOptionPane.showMessageDialog(null, "KILL THE SAU(TRIANGLE THING) TO WIN GAME");
    }
    public void doneSave()
    {
        JOptionPane.showMessageDialog(null, "You Have Saved The Game","Kwazam Chess",JOptionPane.YES_NO_CANCEL_OPTION);
    }

}

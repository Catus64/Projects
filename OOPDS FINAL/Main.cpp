#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <iomanip>
#include <fstream>
#include <cmath>
using namespace std;



/**********|**********|**********|
Program: Main.cpp 
Course: Data Structures and OOP
Trimester: 2410
Name: Wan Abdul Rahman
ID: 1221103634
Name: Eleonore Tan  
ID: 1221104047 
Name: Chan Jun Tien 
ID: 1221103412 
Name: Jason Lam Jia Hao
ID: 1221103818
Lecture Section: TC101
Tutorial Section: TT1L
Email: abc123@yourmail.com
Phone: 018-1234567
*/




//rocks are optional obstacle to speed up the game
struct rocks{
    char symbol = '*';
    string type = "rocks";
};
//class for battlefield
class Battlefield{
    private:
    int width,height;
    public:
    bool rock_setting = false;
    rocks rock;
    int size_setting=0;
    int space_count;
    vector<vector<char> > board;
    //Constructor for battlefield
    Battlefield(int w, int h){
        space_count = 0;
        board.resize(w);
        for (int i = 0; i < w; ++i) {
        board[i].resize(h, '.');
        space_count=space_count+h;
        }
        width = w;
        height = h;
        //size_setting is a variable that modify some behaviour ie navigating_radius and rocks spawned every 10 tile its increased by 1
        int h_S=1,w_S=1;
        while(h-10 >= 0){
            h_S++;
            h = h-10;
        }
        while(w-10 >= 0){
            w_S++;
            w = w-10;
        }
        size_setting = (h_S+w_S)/2;
    }
    //getters
    int get_width(){return width;}
    int get_height(){return height;}
    //displaying the battle field's content
    void display() {
        cout << "┌";
        for(int t = 0; t < (width*4)+3; t++){
            cout << "─";
        }
         cout << "┐";
        for(int i = 0; i < height; i++){
            cout << endl;
            cout << "│";
        for(int j = 0; j < width; j++){
            cout << setw(4) << board[j][i];
            
        }
        cout << setw(3) <<" ";
        cout << "│";
    }
    cout <<endl<< "└";
        for(int t = 0; t < (width*4)+3; t++){
            cout << "─";
        }
    cout << "┘";
    cout << endl;
    cout << endl;
    }
    //clearing squares that are fired
    void clearfire(){
        for(int i = 0; i < height; i++){
        for(int j = 0; j < width; j++){
            if(board[j][i]=='x'){
                board[j][i]='.';
            }
            }
        }
    }
    //checking if a square has been fired (to highlight robot's death)
    bool is_fired(int x,int y){
        if(bound_check(x,y)){
            if(board[x][y]=='x'){
                return true;
            }}
            return false;
    }
    //checking if robots are interacting with rocks
    bool not_rock(int x,int y){
        if(bound_check(x,y)){
            if(board[x][y]=='*'){
                return false;
            }}
            return true;
    }
    //setting a bot or any character into the battlefield(robot can spawn into rocks)
    void setbot(int x,int y,char n) {
        if(bound_check(x,y)){
            board[x][y] = n;     
        }}
    //checking if the current square is occupied or not with any robot/objects
    bool not_occupied(int x,int y) {
        if(!bound_check(x,y)){return false;}
        if(x<0 || y<0 ){return false;}
        //cout << board[x][y] << endl;
        if(board[x][y]=='0'){return true;}
        else{return false;}
    }
    //optional spawning rocks in the battlefield(will spawn rocks depending on battlefield's ize)
    void spawnrocks(){
        for(int i=0;i<(space_count/4);i++){
            int x,y;
            rand_spawn(x,y);
            setbot(x,y,rock.symbol);
        }
        cout << "Spawning rocks.."<<endl <<endl;
    }

    int count_free_space(){
        int space_count = 0;
        for(int i = 0; i < height; i++){
        for(int j = 0; j < width; j++){
            if(board[j][i]=='.'){space_count++;};
        }
    }return space_count;
    }
    void spawnrocks_mini(){
        if(count_free_space() < (space_count/3)){
            cout <<endl<< "Can't Spawn Rocks.."<<endl <<endl;
        }
        else{
        for(int i=0;i<(space_count/10);i++){
            int x,y;
            rand_spawn(x,y);
            setbot(x,y,rock.symbol);
        }
        cout << "Spawning more rocks.."<<endl <<endl;
        }
    }
    // getting random coordinates to spawn anything in thats not occupied (value of ="." means not occupied)
    void rand_spawn(int& x,int& y){
        do{
        x = (rand()%width);
        y = (rand()%height);
        }while(!not_occupied(x,y));
    }
    //checking if the square is within the bounds of the battlefield
    bool bound_check(int x,int y){
        if(x > width-1 || y > height-1){return false;}
        if(x<0 || y < 0){return false;}
        else{return true;}
    }
    //cheking if the square is occupied by bots or not
    bool check_step(int x,int y){
        char r = board[x][y];
        switch(r){
            case 'R':
            return true;
            break;
            case 'T':
            return true;
            break;
            case 'Y':
            return true;
            break;
            case 'M':
            return true;
            break;
            case 'B':
            return true;
            break;
            case 'U':
            return true;
            break;
            case 'K':
            return true;
            case 'S':
            return true;
            case 'P':
            return true;
            break;
        }
        return false;
    }
    };

//Class for base class Robot(Is inherited by every bot)
class Robot{
    private:
    //the positions are private hence hiddem from any other robots
    int positionX;
    int positionY;
    int live_count;
    string type;
    int kill_count; //to count for upgrading
    int step_travelled; //total steps travelled
    public:
    int suffocate=0;
    int total_kill_count; //total bots killed
    string name;
    char symbol;
    bool is_alive;

    //setters and getters 
    virtual int get_step(){return step_travelled;}
    virtual void set_positionX(int x){positionX = x;}
    virtual void set_positionY(int y){positionY = y;}
    virtual void set_type(string t){type = t;}
    virtual string get_type(){return type;}
    virtual int get_positionX(){return positionX;}
    virtual int get_positionY(){return positionY;}
    virtual void set_live_count(int l){live_count = l;}
    virtual int get_live_count(){return live_count;}
    int get_kill_count(){return kill_count;}
    int get_total_kill_count(){return total_kill_count;}
    int get_step_travelled(){return step_travelled;}
    void set_step_travelled(int x){step_travelled = x;}
    void reset_kill_count(){kill_count=0;}
    void set_kill(int x){kill_count = x;}
    void set_kill_count(int x){total_kill_count= x;}
    virtual void kill(){kill_count++;total_kill_count++;}

    //to decrease a life everytime killed
    virtual void killed(){live_count--;}
    //to increase step_travelled
    virtual void move_a_step(){step_travelled++;}
    //pure virtual function for all robots
    virtual void action(Battlefield& A)=0;
    //default spawning message for every bot(triggers when spawned)
    virtual void spawn_message(){
        cout <<get_type() <<" " +name + " Has Spawned " << "at ("<<get_positionX() <<","<<get_positionY()  <<")" << endl;}
    //part of everybot's constructor for inputting values
    virtual void spawn_value(int x,int y,string n, Battlefield& a,string type,char s){
        set_positionX(x);
            set_positionY(y);
            set_type(type);
            name = n;
            symbol=s;
            a.setbot(x,y,s);
            is_alive = true;
            step_travelled = 0;
            kill_count = 0;
            live_count = 3;
    }
    //spawning bots randomly when they re-enter the battlefield
    virtual void robot_respawn(Battlefield& A){
        int x,y;
        //cout << get_positionX() << "," << get_positionY()<<endl;
        do{
        x = rand()%A.get_width();
        y = rand()%A.get_height();
        }while(!A.not_occupied(x,y));
        set_positionX(x);
        set_positionY(y);
        cout << get_type() <<" "<<name<<" is respawning";
        cout <<" at " << get_positionX() << "," << get_positionY() << " LIFE COUNT: " <<get_live_count()<< endl;
        is_alive = true;
        A.setbot(x,y,symbol);
        
    }

    //Destructor mostly used when robots are upgrading
    Robot(){}
    virtual  ~Robot(){cout  << type +" "+name+" is evolving...." << endl;}
};
//Class MovingRobot for robots that can move
class MovingRobot : virtual public Robot{
    private:
    int new_pos_X,new_pos_Y;
    public:
    MovingRobot(){}
    virtual void move(Battlefield&)=0;//pure virtual function to be overriten
    //setters and getters
    void set_new_x(int x){new_pos_X = x;}
    void set_new_y(int y){new_pos_Y = y;}
    int get_new_x(){return new_pos_X;}
    int get_new_y(){return new_pos_Y;}

};
//Class Shooting for robots that can shoot
class ShootingRobot : virtual public Robot{
    private:
    public:
    int fire_X,fire_Y; //to highlight currently shot tiles
    ShootingRobot(){}
    virtual void fire(Battlefield& A)=0;
    virtual ~ShootingRobot(){};
};
//Class Seeing for robots that can look
class SeeingRobot : virtual public Robot{
    public:
    int seen[3][9]; //array to see squares looked
    SeeingRobot(){}
    virtual void look(Battlefield A)=0;//pure virtual function
    virtual bool not_block(){ //to check if the bot can move to any squares 
        int count=0;  //(all unavalaible square has the value of -1 hence -9 means all square the bot as seen cannot be moved to)
        for(int i = 0;i < 9;i++){
        count = count + seen[0][i]; 
        }
        if(count <= -9){
            cout << "This bot is blocked and cannot move"<<count<<endl;
            suffocate++;
            if (suffocate>2){is_alive=false;cout<<"This Robot Has Suffocated";suffocate=0;}
            return false;
        }
        return true;
    }};
//Stepping class for robot that can step on other robot
class SteppingRobot : virtual public Robot{
    public:
    SteppingRobot(){}
    virtual void step()=0; //pure virtual class
};
//Specially made for SharafBot a robot that can explode and kill himself
//Mr.Sharaf always mentions that classes in c++ is a nuclear bomb hence where this idea came from;no offense were meant
//also a nice way to show you respect sir as I respect you very much
class ExplodingRobot : virtual public Robot{
    public:
    virtual void explode(Battlefield& A)=0;
    int radius_e = 2; 
};
//To Navigate and return a square where its occupied by a Robot
class NavigateBot : virtual public Robot{
    public:
    int radius = 3,target_x=-1,target_y=-1;//value for seeing radius(some constructor changes this values) -1 highlights no square is targeted
    virtual void navigate(Battlefield& A)=0;//pure virtual class
    virtual bool target(int x,int y,Battlefield& A)//to check if a square has any robots in it
    {
        if(A.bound_check(x,y)){
            if(A.check_step(x,y)){
                if(x == get_positionX() && y ==get_positionY()){
                    return false;
                }
                target_x = x;
                target_y = y;
                cout << get_type() <<" " +name+ " has found a Target!!"<< endl;
                return true;
            }
        }return false;
    }
};





class RoboCop :public MovingRobot, public ShootingRobot, public SeeingRobot{
public:
    RoboCop(){}
    RoboCop(int x,int y,string n,Battlefield& a){
        spawn_value(x,y,n,a,"Robocop",'R');
        spawn_message();
    }
    
    void look(Battlefield A){ //Looking on a 3x3 square centered on itself
        int y = get_positionY();
        int x = get_positionX();
        cout <<get_type() <<" " +name + " is" << " looking at (" << get_positionX() << "," << get_positionY()<<")" << endl; 
        int temp_y[3] = {y-1,y,y+1};
        int temp_x[3] = {x-1,x,x+1};
        for(int i=0;i<9;i++){
            if(i<3){
                if(A.not_occupied(temp_x[i%3],y-1))
                {seen[0][i]=temp_x[i%3];
                  seen[1][i]=y-1;}
                else{
                    seen[0][i] = -1;
                    seen[1][i] = -1;
                }
                }
            else if(i<6){
                if(A.not_occupied(temp_x[i%3],y)){
                seen[0][i]=temp_x[i%3];
                seen[1][i]=y;}
                else{
                    seen[0][i] = -1;
                    seen[1][i] = -1;
                }
                }
            else if(i<9){
                if(A.not_occupied(temp_x[i%3],y+1)){
                seen[0][i]=temp_x[i%3];
                seen[1][i]=y+1;}
                else{
                    seen[0][i] = -1;
                    seen[1][i] = -1;
                    }
                }
        }   
    }

    void fire(Battlefield& A){//Robocop Firing Pattern
        for(int i = 0;i < 3;i++){
        bool fired = false;
        while(!fired){//fired is the state whether the firing locations are in bounds or not
        fire_X = rand()%11;//random a number 1-10
        fire_Y = rand()%((10-fire_X)+1);//randoming the remaining number from earlier (x+y will not exceed 10)
        int i = rand()%5;//randoming for negative cases
        switch(i){//results of random will decide which coordinates are negative so the robot can shoot everywhere
            case 1:
            break;
            case 2:
            fire_X = fire_X * (-1);
            break;
            case 3:
            fire_Y = fire_Y * (-1);
            case 4:
            fire_X = fire_X * (-1);
            fire_Y = fire_Y * (-1);
        }
        fire_X = get_positionX() + fire_X;
        fire_Y = get_positionY() + fire_Y;
        if(A.bound_check(fire_X,fire_Y)&&A.not_rock(fire_X,fire_Y)){//checking if square is in bounds or occupied by a robot(some robots cant shoot rocks)
            fired = true;
        }
        if(fire_X == get_positionX() && fire_Y == get_positionY()){fired = false;}//so the bot can't fire itself
        }
        if(A.check_step(fire_X,fire_Y)){//checking if robot hit anything
            cout << get_type()<<" "+ name +" shot something at ("<< fire_X<<","<<fire_Y<<")"  << endl;
        }else
        {cout << get_type()<<" "+ name +" fired at (" << fire_X<<","<<fire_Y<<")" << endl;}
        A.setbot(fire_X,fire_Y,'x');//highlighting square shot
        }
    }
    void move(Battlefield& A){//Robocop Moving Pattern
        for(int i = -1;i < 0;){
            int move = rand() % 9;//randomign a square thats received from the look() function (-1 means unavalaible square)
            i = seen[0][move];
            set_new_x(seen[0][move]);//setting moving coordinates
            set_new_y(seen[1][move]);
            }
        A.setbot(get_positionX(),get_positionY(),'.');//removing itself from old location
        A.setbot(get_new_x(),get_new_y(),symbol);//setting at new location
        set_positionX(get_new_x());//changing location in robots attribute
        set_positionY(get_new_y());
        cout << get_type() <<" " + name << " Moves to (" << get_new_x() << "," << get_new_y()<<")" << endl;
        move_a_step();//increasing total squares travelled
        A.display();
        cin.get();
        
    }
    void action(Battlefield& A){//action pattern for Robocop
        if(!is_alive){cout << get_type() <<" " +name+ " is dead and can't move" << endl<<endl;return;}//bots cant move if they're dead
        cout << get_type() <<" " +name+ " is acting" << endl;
        look(A);
        if(not_block()){move(A);}
        fire(A);
        A.display();
    }
};

class Terminator : public MovingRobot, public SteppingRobot, public SeeingRobot{
public:
    Terminator(){}
    Terminator(int x,int y,string n,Battlefield& a){
            spawn_value(x,y,n,a,"Terminator",'T');
            spawn_message();
    }
    
    void look(Battlefield A){//Same with Robocop but Terminator can move to square that have robots Hence squares occupied by bots can be travelled
        int y = get_positionY();
        int x = get_positionX();
        cout << get_type() <<" " +name + " is" << " looking at (" << get_positionX() << "," << get_positionY()<<")" << endl; 
        int temp_y[3] = {y-1,y,y+1};
        int temp_x[3] = {x-1,x,x+1};
        for(int i=0;i<9;i++){
            if(i<3){
                if(A.bound_check(temp_x[i%3],y-1)&&A.not_rock(temp_x[i%3],y-1))//can't move through roks
                {seen[0][i]=temp_x[i%3];
                  seen[1][i]=y-1;}
                else{
                    seen[0][i] = -1;
                    seen[1][i] = -1;
                }
                }
            else if(i<6){
                if(A.bound_check(temp_x[i%3],y)&&A.not_rock(temp_x[i%3],y)){
                seen[0][i]=temp_x[i%3];
                seen[1][i]=y;
                if(temp_x[i%3] == get_positionX()){seen[0][i] = -1;seen[1][i] = -1;}//cant move to other terminator but not itself
                }
                else{
                    seen[0][i] = -1;
                    seen[1][i] = -1;
                }
                }
            else if(i<9){
                if(A.bound_check(temp_x[i%3],y+1)&&A.not_rock(temp_x[i%3],y+1)){
                seen[0][i]=temp_x[i%3];
                seen[1][i]=y+1;}
                else{
                    seen[0][i] = -1;
                    seen[1][i] = -1;
                }
                }
        }
    }

    void move(Battlefield& A){//Same with robocop with addition of step()
        for(int i = -1;i < 0;){
            int move = rand() % 9;
            i = seen[0][move];
            set_new_x(seen[0][move]);
            set_new_y(seen[1][move]);
            }
        for(int i = 0; i < 8;i++){
            if(seen[0][i] == -1){}
            else if(A.check_step(seen[0][i],seen[1][i])){
            set_new_x(seen[0][i]);
            set_new_y(seen[1][i]);
            step();
            break;
            }
            else{}
        }
        cout << get_type() <<" " +name << " Moves to (" << get_new_x() << "," << get_new_y()<<")" << endl;
        A.setbot(get_positionX(),get_positionY(),'.');
        A.setbot(get_new_x(),get_new_y(),symbol);
        set_positionX(get_new_x());
        set_positionY(get_new_y());
        move_a_step();
        A.display();
        cin.get();
    }

    

    void action(Battlefield& A){
        if(!is_alive){cout << get_type() <<" " +name+ " is dead and can't move" << endl<<endl;return;}
        cout << get_type() <<" " +name+ " is acting" << endl;
        look(A);
        if(not_block()){move(A);}
    }
    
    void step(){
        cout << get_type() <<" " +name << " Has stepped something" << endl;//highlight that Terminator have stepped a robot
    }

};

 class BlueThunder : public ShootingRobot{//Blue thunder can't move
    int fire_state=0;//highlight which firing state its in (clockwise)
 public:
    BlueThunder(){}
    BlueThunder(int x,int y,string n,Battlefield& a){
            spawn_value(x,y,n,a,"BlueThunder",'B');
            spawn_message();;
    }
    void fire(Battlefield& A){
        if(fire_state>7){fire_state=0;}
        switch(fire_state){
            case 0:
            fire_X = get_positionX() + 0;
            fire_Y = get_positionY() - 1;
            break;
            case 1:
            fire_X = get_positionX() + 1;
            fire_Y = get_positionY() - 1;
            break;
            case 2:
            fire_X = get_positionX() + 1;
            fire_Y = get_positionY() + 0;
            break;
            case 3:
            fire_X = get_positionX() + 1;
            fire_Y = get_positionY() + 1;
            break;
            case 4:
            fire_X = get_positionX() + 0;
            fire_Y = get_positionY() + 1;
            break;
            case 5:
            fire_X = get_positionX() - 1;
            fire_Y = get_positionY() + 1;
            break;
            case 6:
            fire_X = get_positionX() - 1;
            fire_Y = get_positionY() + 0;
            break;
            case 7:
            fire_X = get_positionX() - 1;
            fire_Y = get_positionY() - 1;
            break;
        }
        if(!A.bound_check(fire_X,fire_Y)&&A.not_rock(fire_X,fire_Y)){
            cout << get_type() << " " << name <<" is trying to shoot out of bounds."<<endl;
            fire_state++;
            return;
        }
        if(A.check_step(fire_X,fire_Y)){
            cout << get_type()<<" "+ name +" shot something at ("<< fire_X<<","<<fire_Y<<")"  << endl;
        }else{cout << get_type()<<" "+ name +" fired at (" << fire_X<<","<<fire_Y<<")" << endl;}
        A.setbot(fire_X,fire_Y,'x');
        fire_state++;//checking fire eligibility and going to the next firing state(clockwise)
    }
    void action(Battlefield& A){//Blue thunder action pattern
        if(!is_alive){cout << get_type() <<" " +name+ " is dead and can't move" << endl<<endl;return;}
        cout << get_type() <<" " +name+ " is acting" << endl;
        fire(A);
        A.display();
    }
 };

 class TerminatorRoboCop : public RoboCop, public Terminator{
    public:
    TerminatorRoboCop(){}
    TerminatorRoboCop(int x,int y,string n,Battlefield& a){
            spawn_value(x,y,n,a,"TerminatorRobocop",'Y');
            spawn_message();
    }
    void look(Battlefield A){}

    void action(Battlefield& A){//inherits his behaviour and moveset from robot and terminator(moves like a terminator and shoot like a robot LITERALLY)
        if(!is_alive){cout << get_type() <<" " +name+ " is dead and can't move" << endl<<endl;return;}
        cout << get_type() <<" " +name+ " is acting" << endl;
        Terminator::look(A);
        if(Terminator::not_block()){Terminator::move(A);}
        RoboCop::fire(A);
        A.display();
        }
 };

  class Madbot : public BlueThunder{
    public:
    Madbot(){}
    Madbot(int x,int y,string n,Battlefield& a){
            spawn_value(x,y,n,a,"Madbot",'M');
            spawn_message();
            }
    void fire(Battlefield& A){//Same as Blue thunder but random value instead of clockwise
        bool fired = false;
        int cap=0;
        while(!fired){
            int roll = rand()%8;
            switch(roll){
            case 0:
            fire_X = get_positionX() + 0;
            fire_Y = get_positionY() - 1;
            break;
            case 1:
            fire_X = get_positionX() + 1;
            fire_Y = get_positionY() - 1;
            break;
            case 2:
            fire_X = get_positionX() + 1;
            fire_Y = get_positionY() + 0;
            break;
            case 3:
            fire_X = get_positionX() + 1;
            fire_Y = get_positionY() + 1;
            break;
            case 4:
            fire_X = get_positionX() + 0;
            fire_Y = get_positionY() + 1;
            break;
            case 5:
            fire_X = get_positionX() - 1;
            fire_Y = get_positionY() + 1;
            break;
            case 6:
            fire_X = get_positionX() - 1;
            fire_Y = get_positionY() + 0;
            break;
            case 7:
            fire_X = get_positionX() - 1;
            fire_Y = get_positionY() - 1;
            break;
        }
        cap++;
        if(cap > 40){return;}
        if(A.bound_check(fire_X,fire_Y)&&A.not_rock(fire_X,fire_Y)){
            fired = true;
        }
        }
        if(A.check_step(fire_X,fire_Y)){
            cout << get_type()<<" "+ name +" shot something at ("<< fire_X<<","<<fire_Y<<")"  << endl;
        }else{cout << get_type()<<" "+ name +" fired at (" << fire_X<<","<<fire_Y<<")" << endl;}
        A.setbot(fire_X,fire_Y,'x');
    }

    void action(Battlefield& A){//Madbot acting patterns
        if(!is_alive){cout << get_type() <<" " +name+ " is dead and can't move" << endl<<endl;return;}
        cout << get_type() <<" " +name+ " is acting" << endl;
        fire(A);
        A.display();
        }

  };

  class RoboTank : public Madbot{
    public:
    RoboTank(){}
    RoboTank(int x,int y,string n,Battlefield& a){
            spawn_value(x,y,n,a,"RoboTank",'K');
            spawn_message();
            }

    void fire(Battlefield& A){//shoot a random spot in the battlefield (can shoot through rocks)
        bool fired = false;
        while(!fired){
        fire_X = rand()%(A.get_width()-1);
        fire_Y = rand()%(A.get_height()-1);
        fired = true;
        if(fire_X == get_positionX() && fire_Y == get_positionY()){fired = false;}
        }
        if(!A.not_rock(fire_X,fire_Y)){fired = false;}
        if(A.check_step(fire_X,fire_Y)){
            cout << get_type()<<" "+ name +" shot something at ("<< fire_X<<","<<fire_Y<<")"  << endl;
        }else{cout << get_type()<<" "+ name +" fired at (" << fire_X<<","<<fire_Y<<")" << endl;}
        A.setbot(fire_X,fire_Y,'x');
    }

    void action(Battlefield& A){//action pattern for RoboTank
        //set_live_count(1);
        if(!is_alive){cout << get_type() <<" " +name+ " is dead and can't move" << endl<<endl;return;}
        cout << get_type() <<" " +name+ " is acting" << endl;
        fire(A);
        A.display();
    }
   };

   class UltimateRobot : public RoboTank, public TerminatorRoboCop{//The Strongest bot there is (sniper bot is stronger)
    int fire_x,fire_y; //overite because of ambiguity(Bad Practice!!)
    public:
    UltimateRobot(){}
    UltimateRobot(int x,int y,string n,Battlefield& a){
            spawn_value(x,y,n,a,"UltimateRobot",'U');
            spawn_message();
            }
    void fire(Battlefield A){//Fires like a Robocop than Shoot Randomly Three times(Can Shoot Through Rocks)
        RoboCop::fire(A);
        bool fired = false;
        for(int i = 0;i < 3;i++){
        fired = false;
        while(!fired){
        fire_x = rand()%(A.get_width()-1);
        fire_y = rand()%(A.get_height()-1);
        fired = true;
        if(fire_x == get_positionX() && fire_y == get_positionY())
        {fired = false;}
        if(!A.not_rock(fire_x,fire_y)){fired = false;}
        }
        if(A.check_step(fire_x,fire_y)){
            cout << get_type()<<" "+ name +" shot something at ("<< fire_x<<","<<fire_y<<")"  << endl;
        }else{cout << get_type()<<" "+ name +" fired at (" << fire_x<<","<<fire_y<<")" << endl;}
        A.setbot(fire_x,fire_y,'x');
        }
        A.display();
        A.clearfire();
    }

    void action(Battlefield& A){//action pattern for UltimateRobot
        if(!is_alive){cout << get_type() <<" " +name+ " is dead and can't move" << endl<<endl;return;}
        cout << get_type() <<" " +name+ " is acting" << endl;
        Terminator::look(A);
        if(Terminator::not_block()){Terminator::move(A);}
        fire(A);
        }

   };
    //Legendary SharafBot Class (Fun Fact:The SharafBot cannot spawn by itself but has a 1/100 chance to spawn in a simulation)
    //It is made to speed up the unimaginably long and dragged out nature of the game
   class SharafBot: public MovingRobot,public ExplodingRobot,public NavigateBot,public SeeingRobot{
    public:
    SharafBot(){}
    SharafBot(int x,int y,string n,Battlefield& a){//has no spawn message hehehe
            spawn_value(x,y,n,a,"SharafBot",'S');
            printsharaft();
            set_live_count(3);
            radius = a.size_setting+5;//navigating is based on the size of the battlefield(size setting is a variable that changes little things in the simulation)
            }
    void look(Battlefield A)//Looks like a robocop
    {
        int y = get_positionY();
        int x = get_positionX();
        cout <<get_type() <<" " +name + " is" << " looking at (" << get_positionX() << "," << get_positionY()<<")" << endl; 
        int temp_y[3] = {y-1,y,y+1};
        int temp_x[3] = {x-1,x,x+1};
        for(int i=0;i<9;i++){
            if(i<3){
                if(A.not_occupied(temp_x[i%3],y-1))
                {seen[0][i]=temp_x[i%3];
                  seen[1][i]=y-1;}
                else{
                    seen[0][i] = -1;
                    seen[1][i] = -1;
                }
                }
            else if(i<6){
                if(A.not_occupied(temp_x[i%3],y)){
                seen[0][i]=temp_x[i%3];
                seen[1][i]=y;}
                else{
                    seen[0][i] = -1;
                    seen[1][i] = -1;
                }
                }
            else if(i<9){
                if(A.not_occupied(temp_x[i%3],y+1)){
                seen[0][i]=temp_x[i%3];
                seen[1][i]=y+1;}
                else{
                    seen[0][i] = -1;
                    seen[1][i] = -1;
                    }
                }
        }   
    }

    void printsharaft(){//SharafBot spawn message to notify the user it is spawned(intentionally made big so user would notice)
                        //it is quite the rare occurence after all (1 in 100!!!!!)

    cout << endl << endl << "OH no....something is happening..." << endl << endl;
    cin.get();


    cout<<"                            ....\n"                         ;//this is an ascii art based of Mr.Sharaf's picture(someone took from online class)
    cout<<"                        ........... .\n"                   ;//This is Mr.Sharaf looking at his monitor
    cout<<"                    . ..,.,,.****,,,, .\n"                  ;
    cout<<"                    ...*****//////**,*,.,\n"               ;  
    cout<<"                   . *,*(/((((((((((/*/*     \n"             ;
    cout<<"                  . ///(((((/(#((((/*/,,     \n"            ;
    cout<<"                    .,/###%%(((#%%&%##(# .  \n"              ;
    cout<<"                    ./(////(////%*(/((*,,    \n"             ;
    cout<<"                    .*/*(((/(##(((#(/         \n"           ;
    cout<<"                .. ,#*/((#%%%%%%#%/ .          \n"        ;
    cout<<"            .  ,,*,(**#(**(###%&%##/#%%(*** .   \n"        ; 
    cout<<"        ..****,/*, */*(%((((///(//#(####///(/, , \n"        ;
    cout<<"        .,,**,**(/* **,/##((####&&#(%%%%##*** /,  \n"       ;
    cout<<"        ,//**/**//##(#%#((####%(##%#(##%#/#//((*/..\n"      ;
    cout<<"        ,/*/(/**,**///##(#####(((//(#####/%#((**//* .\n"    ;
    cout<<"        ,/((/*(/**,,**((/((%#(#((#((##(/(###%((/(*(/* .\n"  ;
    cout<<"        *%%%(/*,*******/***/////(####/((##%%#(&%##%#((/ \n";
    cout <<"!!!!!!!!!!!!!!!SHARAF BOT HAS SPAWNED!!!!!!!!!!!!!!!!!!!!!!!"<<endl<<endl;
    cin.get();


    }

    void move(Battlefield& A){//SharafBot moves like a robocop except it prefers square that is nearer to other robot(so his explosion can kill)
        double h,h1 = 100;
        int x,y;
        int a_x,b_y,ab;
        if(target_x !=-1){
        for(int i = 0;i < 9;i++){
            if(seen[0][i]== -1){}
            else{
            int x = seen[0][i];
            int y = seen[1][i];
            a_x = abs(x - target_x);
            b_y = abs(y - target_y);
            ab = a_x*a_x + b_y*b_y;
            //cout << ab <<endl;
            h = sqrt(ab);//calc hipotnus
            if(h < h1){
                set_new_x(seen[0][i]);
                set_new_y(seen[1][i]);
                h1 = h;
                }
            }}//using phythogoras theorem to find which coordinate in seen is closest to target(with hipotnus!!)
        }else{
            cout << get_type() <<" " + name << " did not found any target.."<<endl;//if no target(targetx or y=-1) will move like a robocop
            for(int i = -1;i < 0;){
            int move = rand() % 9;
            i = seen[0][move];
            set_new_x(seen[0][move]);
            set_new_y(seen[1][move]);
            }
        }//same moving procedure
        A.setbot(get_positionX(),get_positionY(),'.');
        A.setbot(get_new_x(),get_new_y(),symbol);
        set_positionX(get_new_x());
        set_positionY(get_new_y());
        cout << get_type() <<" " + name << " Moves to (" << get_new_x() << "," << get_new_y()<<")" << endl;
        move_a_step();
        A.display();
        cin.get();
    }
    void navigate(Battlefield& A)
    {
        cout << get_type() <<" " +name+ " is Navigating.." << endl;
        int ori_x = get_positionX();
        int ori_y = get_positionY();
        int tar_x,tar_y;
        for(int i = 0;i < radius;i++){
            for(int i2= 0;i2 < radius;i2++){//A very dumb code to check in a radiusxradius if theres any bots nearby (can only target one at a time)
                tar_x = ori_x+i2;
                tar_y = ori_y+i;
                //A.setbot(tar_x,tar_y,'x');
                if(target(tar_x,tar_y,A)){return;}
                tar_x = ori_x-i2;
                tar_y = ori_y-i;
                //A.setbot(tar_x,tar_y,'x');
                if(target(tar_x,tar_y,A)){return;}
                tar_x = ori_x+i2;
                tar_y = ori_y-i;
                //A.setbot(tar_x,tar_y,'x');
                if(target(tar_x,tar_y,A)){return;}
                tar_x = ori_x-i2;
                tar_y = ori_y+i;
                //A.setbot(tar_x,tar_y,'x');
                if(target(tar_x,tar_y,A)){return;}

                tar_x = ori_x;
                tar_y = ori_y+i;
                //A.setbot(tar_x,tar_y,'x');
                if(target(tar_x,tar_y,A)){return;}

                tar_x = ori_x;
                tar_y = ori_y-i;
                //A.setbot(tar_x,tar_y,'x');
                if(target(tar_x,tar_y,A)){return;}
            }
        }
        A.display();
    }
    void explode(Battlefield& A)//exploding squares around him depending on his explosion radius 
    {                           //Can destroy rock(Obvioulsy)
        cout << get_type() <<" " +name+ " Has Exploded!!!" << endl;
        int ori_x = get_positionX();
        int ori_y = get_positionY();
        int tar_x,tar_y;
        for(int i = 0;i < radius_e;i++){
            for(int i2= 0;i2 < radius_e;i2++){
                tar_x = ori_x+i2;
                tar_y = ori_y+i;
                A.setbot(tar_x,tar_y,'x');

                tar_x = ori_x-i2;
                tar_y = ori_y-i;
                A.setbot(tar_x,tar_y,'x');

                tar_x = ori_x+i2;
                tar_y = ori_y-i;
                A.setbot(tar_x,tar_y,'x');

                tar_x = ori_x-i2;
                tar_y = ori_y+i;
                A.setbot(tar_x,tar_y,'x');

                tar_x = ori_x;
                tar_y = ori_y+i;
                A.setbot(tar_x,tar_y,'x');

                tar_x = ori_x;
                tar_y = ori_y-i;
                A.setbot(tar_x,tar_y,'x');

                A.setbot(get_positionX(),get_positionY(),symbol);
            }
        }
        A.display();
        cin.get();
    }

    void suicide(Battlefield& A){//After every explosion have a chance to kill itself
        int chance = (3+A.size_setting)-radius_e;
            if(chance <= 0){chance = 1;}
            if(rand()%chance == 0){
                A.setbot(get_positionX(),get_positionY(),'x');
                cout << get_type() <<" " +name+ " has killed himself in the explosion"<<endl;
                is_alive = false;
                set_live_count(1);
                return;
            }
        cout << get_type() <<" " +name+ " survives the explosion and will explode bigger!!!"<<endl;
        radius_e++;//if it survives the explosion gets bigger but dont worry its capped depending on the map size
        if(radius_e > A.size_setting+3){radius_e--;}
        return;
    }

    void action(Battlefield& A){//Sharaf bot action pattern
        if(!is_alive){cout << get_type() <<" " +name+ " is dead and can't move" << endl<<endl;return;}
        look(A);
        navigate(A);
        A.display();
        if(not_block()){move(A);}
        if(rand()%3==1){
        explode(A);
        suicide(A);
        }
        target_x = -1;//resetting target value (so the bot doens't target nothing)
        target_y = -1;
    };
   };

class SniperBot : public ShootingRobot, public NavigateBot, public MovingRobot, public SeeingRobot
{
    public:
    SniperBot(int x,int y,string n,Battlefield& a){//Sniper Bot OUR GREATEST CREATION
            spawn_value(x,y,n,a,"SniperBot",'P');
            spawn_message();
            radius = a.size_setting+1;//can't see as far ahead as Sharaf Bot(too op!!)
            bool sniped = false;
    }
    bool sniped;//check if the shot is successful
    void look(Battlefield A){//Same as Robocop's
        int y = get_positionY();
        int x = get_positionX();
        cout <<get_type() <<" " +name + " is" << " looking at (" << get_positionX() << "," << get_positionY()<<")" << endl; 
        int temp_y[3] = {y-1,y,y+1};
        int temp_x[3] = {x-1,x,x+1};
        for(int i=0;i<9;i++){
            if(i<3){
                if(A.not_occupied(temp_x[i%3],y-1))
                {seen[0][i]=temp_x[i%3];
                  seen[1][i]=y-1;}
                else{
                    seen[0][i] = -1;
                    seen[1][i] = -1;
                }
                }
            else if(i<6){
                if(A.not_occupied(temp_x[i%3],y)){
                seen[0][i]=temp_x[i%3];
                seen[1][i]=y;}
                else{
                    seen[0][i] = -1;
                    seen[1][i] = -1;
                }
                }
            else if(i<9){
                if(A.not_occupied(temp_x[i%3],y+1)){
                seen[0][i]=temp_x[i%3];
                seen[1][i]=y+1;}
                else{
                    seen[0][i] = -1;
                    seen[1][i] = -1;
                    }
                }
        }   
    }
    void fire(Battlefield& A){//Will shot based off target navigation
        if(target_x ==-1){
            cout << get_type() <<" " + name << " do not have any targets... " << endl;//The bot will not shoot if there's not target
            A.display();
            cin.get();
            return;
        }
        if(rand()%5 == 1){
            A.setbot(target_x,target_y,'x');//1 in 5 chances to shoot accurately(this is very strong)
            cout << get_type() <<" " + name << " sniped a target with accuracy!!" << endl;
            sniped = true;//hinting the bot successfully sniped a target
        }else{
            for(int i=0;i<2;i++){//will miss the targeted bot one square away from the actual bot 2 times(can still hit nearby bots)
            int pos = rand()%10;
            switch (pos)
            {
            case 1:
                if(!A.not_rock(fire_X,fire_Y)){break;}
                A.setbot(target_x+1,target_y,'x');
            break;
            case 2:
                if(!A.not_rock(fire_X,fire_Y)){break;}
                A.setbot(target_x+1,target_y+1,'x');
            break;
            case 3:
                if(!A.not_rock(fire_X,fire_Y)){break;}
                A.setbot(target_x,target_y+1,'x');
            break;
            case 4:
                if(!A.not_rock(fire_X,fire_Y)){break;}
                A.setbot(target_x-1,target_y+1,'x');
            break;
            case 5:
                if(!A.not_rock(fire_X,fire_Y)){break;}
                A.setbot(target_x-1,target_y-1,'x');
            break;
            case 6:
                if(!A.not_rock(fire_X,fire_Y)){break;}
                A.setbot(target_x-1,target_y,'x');
            break;
            case 7:
                if(!A.not_rock(fire_X,fire_Y)){break;}
                A.setbot(target_x+1,target_y-1,'x');
            break;
            case 8:
                A.setbot(target_x,target_y-1,'x');
            break;
            }
            }
            cout << get_type() <<" " + name << " missed" << endl;
        }
        A.display();
        cin.get();

    }
    void move(Battlefield& A){//has a 1 in 2 chance of not moving(snipers likes to camp)
        float h,h1 = 100;
        int x,y;
        int a_x,b_y;

        if(rand()%2==1){
        for(int i = -1;i < 0;){
        int move = rand() % 9;
        i = seen[0][move];
        set_new_x(seen[0][move]);
        set_new_y(seen[1][move]);
        }

        A.setbot(get_positionX(),get_positionY(),'.');
        A.setbot(get_new_x(),get_new_y(),symbol);
        set_positionX(get_new_x());
        set_positionY(get_new_y());
        cout << get_type() <<" " + name << " Moves to (" << get_new_x() << "," << get_new_y()<<")" << endl;
        move_a_step();
        A.display();
        cin.get();
        }else{
            cout << get_type() <<" " + name +" is camping for targets...." <<endl; 
            cin.get();
        }
    }
    void navigate(Battlefield& A){
        cout << get_type() <<" " +name+ " is Navigating.." << endl;
        int ori_x = get_positionX();
        int ori_y = get_positionY();
        int tar_x,tar_y;
        for(int i = 0;i < radius;i++){
            for(int i2= 0;i2 < radius;i2++){//navigates like SharafBots
                tar_x = ori_x+i2;
                tar_y = ori_y+i;
                if(target(tar_x,tar_y,A)){return;}
                tar_x = ori_x-i2;
                tar_y = ori_y-i;
                if(target(tar_x,tar_y,A)){return;}
                tar_x = ori_x+i2;
                tar_y = ori_y-i;
                if(target(tar_x,tar_y,A)){return;}
                tar_x = ori_x-i2;
                tar_y = ori_y+i;
                if(target(tar_x,tar_y,A)){return;}
                tar_x = ori_x;
                tar_y = ori_y+i;
                if(target(tar_x,tar_y,A)){return;}
                tar_x = ori_x;
                tar_y = ori_y-i;
                if(target(tar_x,tar_y,A)){return;}
            }
        }
    }
    void action(Battlefield& A){//Sniperbot acting pattern
        if(!is_alive){cout << get_type() <<" " +name+ " is dead and can't move" << endl<<endl;return;}
        look(A);
        navigate(A);
        fire(A);
        if(sniped){
            cout << get_type() <<" " + name + " feels happy and doesn't want to move" <<endl;//The robot will not move after a sucessful snipe(he's just lazy)
            cin.get();
        }
        else{
            if(not_block()){move(A);}
        }
        A.display();
        sniped = false;
        target_x = -1;
        target_y = -1;
    }
    
};

//## LINKED LIST AND QUEUES ##############################################
struct node{
        Robot* robot;
        node* next;
        string r_name,r_type;
        int r_x,r_y;
    };
class Queue{
    public:
    node *front,*rear;
    Queue(){
        front = rear = nullptr; 
    }
    void enqueue(Robot* r){
        // Create a new LL node
        node* temp = new node();
        temp->robot = r;
 
        // If queue is empty, then
        // new node is front and rear both
        if (rear == nullptr) {
            front = rear = temp;
            return;
        }  
        // Add the new node at
        // the end of queue and change rear
        rear->next = temp;
        rear = temp;
    }

    void enqueue1(node* r){
        // Create a new LL node
        node* temp = new node();
        temp = r;
 
        // If queue is empty, then
        // new node is front and rear both
        if (rear == nullptr) {
            front = rear = temp;
            return;
        }  
        // Add the new node at
        // the end of queue and change rear
        rear->next = temp;
        rear = temp;
    }
    void dequeue(){
        // If queue is empty, return NULL.
        if (front == nullptr)
            return;
 
        // Store previous front and
        // move front one node ahead
        node* temp = front;
        front = front->next;
 
        // If front becomes NULL, then
        // change rear also as NULL
        if (front == nullptr)
            rear = nullptr;
        delete (temp);
    }
};
class circular_linked_list{
    public:
        int steps;
        int size;
        node* head;
        node* turn;
        Queue q_done;
        circular_linked_list(int s){
            head = nullptr;
            size = 0;
            steps = s;
        }
        void push(Robot* r)
            {   
                size++;
                // Create a new node and make head
                // as next of it.
                node* ptr1 = new node();
                ptr1->robot = r;
                ptr1->next = head;

                // If linked list is not NULL then
                // set the next of last node
                if (head != nullptr) {
                    // Find the node before head and
                    // update next of it.
                    node* temp = head;
                    while (temp->next != head)
                        temp = temp->next;
                    temp->next = ptr1;
                }
                else
                    // For the first node
                    ptr1->next = ptr1;
                head = ptr1;
            }
        // Function to print nodes in a given
        // circular linked list

        void cleanbattlefields(Queue& q){
            node* botcursor = head;
            do{
                if(!botcursor->robot->is_alive){
                    cout <<botcursor->robot->get_type()<<" "<<botcursor->robot->name<<" is recovering"<<endl;
                    q.enqueue(botcursor->robot);
                    deleteNode(botcursor->robot);
                    botcursor = head;
                    //return;
                }
                botcursor = botcursor->next;
            }while(botcursor != head);
            cout << endl;
        }

        void printList(ofstream& File) //printing the state of the robots in battlefield(will occur every turn)
        {
            node* temp = head;
            cout <<endl<< "Current Robot in Battlefield: " <<endl;
            int count = 1;
            if (head != nullptr) {
                do {
                    cout <<setw(3)<< count <<": "<<temp->robot->get_type()<<" "<< temp->robot->name << " " 
                    <<endl<<setw(3)<<"   ("<< temp->robot->get_positionX() <<","<<temp->robot->get_positionY() << ") " << "life: " << temp->robot->get_live_count() <<" Total Kills: "<<temp->robot->get_total_kill_count()<<endl;
                    count++;
                    File <<setw(3)<< count <<": "<<temp->robot->get_type()<<" "<< temp->robot->name << " " 
                    <<endl<<setw(3)<<"   ("<< temp->robot->get_positionX() <<","<<temp->robot->get_positionY() << ") " << "life: " << temp->robot->get_live_count() <<" Total Kills: "<<temp->robot->get_total_kill_count()<<endl;
                    temp = temp->next;
                } while (temp != head);
            }else{
            cout <<"list is empty" << endl;
            }
            cout << endl;
        }

        void bots_fired(Battlefield& A,Robot* turn,ofstream& File){//checking for which bots is fired in the battlefield
            node* botcursor = head;
            do{

                if(A.is_fired(botcursor->robot->get_positionX(),botcursor->robot->get_positionY()))
                {
                    cout <<botcursor->robot->get_type()<<" "<< botcursor->robot->name << " Was Shot By "
                    <<turn->get_type()<<" "<< turn->name << " "<< endl;
                    File <<botcursor->robot->get_type()<<" "<< botcursor->robot->name << " Was Shot By "
                    <<turn->get_type()<<" "<< turn->name << " "<< endl;
                    turn->kill();
                    botcursor->robot->killed();
                    botcursor->robot->is_alive = false;//higlighting the bot is dead
                    botcursor->robot->set_positionX(-1);//the bot's position will be outside of battlefield
                    botcursor->robot->set_positionY(-1);             
                }
                botcursor = botcursor->next;
            }while(botcursor != head);
        }
        void bots_stepped(Robot* turn,ofstream& File){//checking for shich bot is stepped in the battlefield
            node* botcursor = head;
            int turn_x = turn->get_positionX();
            int turn_y = turn->get_positionY();
            do{
                int bot_x = botcursor->robot->get_positionX();//checking which bot stepped by whom
                int bot_y = botcursor->robot->get_positionY();
                if(bot_x == turn_x && bot_y == turn_y && bot_x != -1)
                {
                    if(turn->name == botcursor->robot->name){}
                    else{
                    cout <<botcursor->robot->get_type()<<" "<< botcursor->robot->name << " Was Stepped By "
                    <<turn->get_type()<<" "<< turn->name << " "<<endl;
                    File <<botcursor->robot->get_type()<<" "<< botcursor->robot->name << " Was Stepped By "
                    <<turn->get_type()<<" "<< turn->name << " "<<endl;
                    turn->kill();
                    botcursor->robot->killed();
                    botcursor->robot->is_alive = false;
                    botcursor->robot->set_positionX(-1);
                    botcursor->robot->set_positionY(-1);
                    }
                }
                botcursor = botcursor->next;
            }while(botcursor != head);
        }
        bool respawn(Battlefield& A,Queue& q){//checking if theres any bots in the respawning queues and put them back into the linklist infront(repawned bots move first)
            if(q.front == nullptr){cout << "no bots respawning .. " <<endl<<endl;return false;}
            q.front->robot->robot_respawn(A);
            push(q.front->robot);
            //printList();
            q.dequeue();
            cin.get();
            return true;
        }

        void print_result(ofstream &File){
            cout <<endl<<endl<< "=========RESULT OF SIMULATION========"<<endl<<endl;
            cout <<endl<<endl<< "=========ROBOT IN BATTLEFIELD========"<<endl<<endl;
            File <<endl<<endl<< "=========ROBOT IN BATTLEFIELD========"<<endl<<endl;
            node* botcursor = head;
            int count = 0;
            do{
                cout <<setw(3)<< count <<": "<<botcursor->robot->get_type()<<" "<< botcursor->robot->name << " " 
                    <<endl<<setw(3)<<"   ("<< botcursor->robot->get_positionX() <<","<<botcursor->robot->get_positionY() << ") " 
                    << "life: " << botcursor->robot->get_live_count() 
                    <<" Total Kills: "<<botcursor->robot->total_kill_count<<endl
                    <<"    Total Step Travelled "<<botcursor->robot->get_step_travelled()<<endl<<endl;

                File <<setw(3)<< count <<": "<<botcursor->robot->get_type()<<" "<< botcursor->robot->name << " " 
                    <<endl<<setw(3)<<"   ("<< botcursor->robot->get_positionX() <<","<<botcursor->robot->get_positionY() << ") " 
                    << "life: " << botcursor->robot->get_live_count() 
                    <<" Total Kills: "<<botcursor->robot->total_kill_count<<endl
                    <<"    Total Step Travelled "<<botcursor->robot->get_step_travelled()<<endl<<endl;

                    count++;
                    botcursor=botcursor->next;
            }while(botcursor != head);
            cout <<endl<<endl<< "==============DEAD BOTS============="<<endl<<endl;
            File <<endl<<endl<< "==============DEAD BOTS============="<<endl<<endl;
            while(q_done.front != nullptr){

                cout <<setw(3)<< count <<": "<<q_done.front->robot->get_type()<<" "<< q_done.front->robot->name << " " 
                <<endl<<setw(3)
                << "life: " << q_done.front->robot->get_live_count() 
                <<" Total Kills: "<<q_done.front->robot->total_kill_count<<endl
                <<"   Total Step Travelled "<<q_done.front->robot->get_step_travelled()<<endl<<endl;

                File <<setw(3)<< count <<": "<<q_done.front->robot->get_type()<<" "<< q_done.front->robot->name << " " 
                <<endl<<setw(3)
                << "life: " << q_done.front->robot->get_live_count() 
                <<" Total Kills: "<<q_done.front->robot->total_kill_count<<endl
                <<"   Total Step Travelled "<<q_done.front->robot->get_step_travelled()<<endl<<endl;
                q_done.dequeue();
                count++;
            }
        }

        void checkdead(){//after every turn will remove bots that are dead and cannot return
            node* botcursor = head;
            do{
                if(botcursor->robot->get_live_count() == 0){
                    cout <<botcursor->robot->get_type()<<" "<<botcursor->robot->name<<" has ran out of lives"<<endl;
                    q_done.enqueue(botcursor->robot);
                    deleteNode(botcursor->robot);
                    botcursor = head;
                    //return;
                }
                botcursor = botcursor->next;
            }while(botcursor != head);
            cout << endl;
        }

        void upgrade(Robot*& robot,Battlefield& A){//upgrading certrain robots to other robot classes while carrying the attributes
            if(robot->get_kill_count()>=3){
                robot->reset_kill_count();
                cout << endl << "WHAT?"<<endl;
                cout << robot->get_type() << " " << robot->get_kill_count()<<" "<<robot->total_kill_count;
                cin.get();

                int x = robot->get_positionX();
                int y = robot->get_positionY();
                int live = robot-> get_live_count();
                string name1 = robot->name;
                int total_kill = robot->total_kill_count;
                int step_travelled = robot->get_step_travelled();
                int up = 0;

                if((robot->get_type() == "Robocop") || (robot->get_type() == "Terminator")){up = 1;}
                else if((robot->get_type() == "RoboTank")){up = 2;}
                else if(robot->symbol=='Y'){up=2;}
                else if((robot->get_type()) == "BlueThunder"){up = 3;}
                else if((robot->get_type()) == "Madbot"){up = 4;}
                else{return;}
                cout << robot->get_type() << " " << robot->name << " is evolving!" << endl <<endl;
                delete robot;
                cout<<up<<endl;
                switch(up){
                case 1:
                robot = new TerminatorRoboCop(x,y,name1,A);
                break;
                case 2:
                robot = new UltimateRobot(x,y,name1,A);
                break;
                case 3:
                robot = new Madbot(x,y,name1,A);
                break;
                case 4:
                robot = new RoboTank(x,y,name1,A);
                break;
                default:
                break;
                }
                robot->total_kill_count = total_kill;
                robot->set_step_travelled(step_travelled);
                cin.get();
            }       
        }
        void spawnsharaf(Battlefield& A){//the odds of spawning SharafBot in (1 in 100!!)
            if(rand()%100==1){
                Robot* r;
                int x,y;
                A.rand_spawn(x,y);
                r = new SharafBot(x,y,"Sharaf",A);
                push(r);
            }
        }

        void simulate(Battlefield& A,Queue& q){//a very clutted simulation function for the robots
            ofstream Result("Result.txt");
            ofstream File("Turn.txt");
            int i3;
            cout << endl << endl << "==========ROBOT WAR SIMULATION IS BEGINNING========="<<endl<<endl;  
            node* botcursor;
            for(int i = 0;i < steps;i++){//looping for turn
                cout << "Next Turn :" << endl;
                cin.get();
                botcursor = head;
                if(head == nullptr){//check if simulation started with no robot in it
                    cout << "There is no more robots in the simulation" << endl;
                    break;}
                if(respawn(A,q)){//respawning robots back into the battlefield
                botcursor = head;
                }
                if(botcursor->next == botcursor){//checking if a bot has won(only one node left in linked list)
                    if(q.front == nullptr){
                    cout <<botcursor->robot->get_type()<<" " << botcursor->robot->name << " HAS WON THE GAME" <<endl;
                    break;
                    }
                }
                spawnsharaf(A);//chance to spawn sharafbot(never ran a simulation where sharafbot wins)
                File << endl << "=========TURN " <<i+1 << "========="<<endl;
                cout << endl << "=========TURN " <<i+1 << "========="<<endl;

                do{
                A.setbot(botcursor->robot->get_positionX(),botcursor->robot->get_positionY(),botcursor->robot->symbol);
                botcursor = botcursor->next;
                }while(botcursor != head);
                botcursor = head;

                printList(File);
                A.display();
                cin.get();

                do{//looping for every bot in a turn
                cout <<endl<< "---------Next Robot---------" << endl;
                cin.get();
                cout << "         ------         "<<endl;
                cout << botcursor->robot->get_type() <<" "<< botcursor->robot->name << "'s turn"<<endl;//highlighting bot's turn
                cout << "         ------         "<<endl;
                botcursor->robot->action(A);
                cout << endl;
                //checking for bots fired
                bots_fired(A,botcursor->robot,File);
                //checking for bots stepped
                bots_stepped(botcursor->robot,File);
                //clearing all spots that are fired (x)
                A.clearfire();
                //checking if the robot can upgrade after it's turn
                upgrade(botcursor->robot,A);
                botcursor = botcursor->next;
                }while(botcursor != head);
                cout << endl << "=========TURN END========="<<endl;
                //getting rid of dead robots   
                checkdead();      //check dead robots and send them away (not respawning)
                cleanbattlefields(q);//check robots that are shot/stepped(can respawn)
                i3=i;
                if(A.rock_setting){
                if(((i+1)%10)==0){
                    A.spawnrocks_mini();
                }}
            }
            File.close();
            cout << endl << endl << "==========ROBOT WAR SIMULATION HAS ENDED========="<<endl<<endl;
            cout  << "==========TURN "<<i3+1<<" ========="<<endl;
            print_result(Result);
            Result.close();
        }   
        // Function to delete a given node
        // from the list
        void deleteNode(Robot* key)
        {
            // If linked list is empty
            if (head == nullptr)
                return;

            // If the list contains only a
            // single node
            if ((head)->robot == key && (head)->next == head) {
                free(head);
                head = nullptr;
                size--;
                return;
            }
            node *last = head, *d;

            // If head is to be deleted
            if ((head)->robot == key) {

                // Find the last node of the list
                while (last->next != head)
                    last = last->next;

                // Point last node to the next of
                // head i.e. the second node
                // of the list
                last->next = (head)->next;
                free(head);
                head = last->next;
                return;
            }

            // Either the node to be deleted is
            // not found or the end of list
            // is not reached
            while (last->next != head && last->next->robot != key) {
                last = last->next;
            }

            // If node to be deleted was found
            if (last->next->robot == key) {
                d = last->next;
                last->next = d->next;
                delete d;
                size--;
            }
            else
                cout << "Given node is not found in the list!!!\n";
        }       
};

class FileReader
{
private:
public:
    int height, width, steps, robotCount, Actualcount=0;
    void InitializeFile(const string &filename,Queue& robot_list)
    {
        ifstream file(filename);
        if (!file.is_open())
        {
            cerr << "Failed to open file: " << filename << endl;
            return;
        }

        string line;
        int lineNumber = 0;

        while (getline(file, line))
        {
            vector<string> words;
            string word;
            for (size_t i = 0; i < line.length(); i++)
            {
                if (line[i] == ' ')
                {
                    if (!word.empty())
                    {
                        words.push_back(word);
                        word.clear();
                    }
                }
                else
                {
                    word += line[i];
                }
            }
            if (!word.empty())
            {
                words.push_back(word);
            }

            if (lineNumber == 0 && words.size() == 6 && words[0] == "M" && words[1] == "by")
            {
                height = stoi(words[4]);
                width = stoi(words[5]);
                cout <<"Heights: "<< height << " Width: " << width << endl;
            }
            else if (lineNumber == 1 && words.size() == 2 && words[0] == "steps:")
            {
                steps = stoi(words[1]);
                cout << "Number of steps: "<<steps << endl;
            }
            else if (lineNumber == 2 && words.size() == 2 && words[0] == "robots:")
            {
                robotCount = stoi(words[1]);
                cout <<"Number of robots: "<< robotCount << endl;
            }
            else if (lineNumber > 2 && words.size() >= 3)
            {
                string type = words[0];
                string name = words[1];
                int positionX, positionY;
                //cout << words[2] << " , "<<words[3]<< endl;

                if(words[2] == "random")
                {
                    positionX = rand() % height;
                }
                else
                {
                    positionX = stoi(words[2]);
                }

                char firstletter = words[3].at(0);
            
                if (firstletter == 'r')
                {
                    positionY = rand() % height;
                }
                else
                {
                    positionY = stoi(words[3]);
                }
                
                node* temp;
                temp = new node;
                temp->r_x = positionX;
                temp->r_y = positionY;
                temp->r_type = type;
                temp->r_name = name;
                robot_list.enqueue1(temp);
                Actualcount++;
                cout << type <<" "<< name <<" "<< positionX<< " " << positionY << endl;
            }

            ++lineNumber;
        }
    }
};



int main(){
    /* For Debugging robot behaviour
    srand(time(0));
    Queue robot_q;
    Queue robot_list;
    Battlefield A(10,10);
    cout << A.size_setting<<" " << A.space_count<<endl;
    A.spawnrocks();
    A.display();

    
    circular_linked_list cll(100);
    cout << A.size_setting << endl;

    Robot *robot1;
    Robot *robot2;
    Robot *robot3;
    Robot *robot4;
    Robot *robot5;
    robot1 = new RoboCop(3,3,"Star",A);
    robot2 = new UltimateRobot(8,2,"Star",A);
    robot3 = new Terminator(2,6,"Star",A);
    robot4 = new SniperBot(4,4,"Sharaf",A);
    cll.push(robot4);
    cll.push(robot3);
    cll.push(robot1);
    cll.push(robot2);
    cll.simulate(A,robot_q);
    */
    
    srand(time(0));
    Queue robot_q;
    Queue robot_list;

    FileReader F;
    F.InitializeFile("robot.txt",robot_list);
    Battlefield A(F.width,F.height);
    circular_linked_list cll(F.steps);
    
    for(int i = 0;i < F.Actualcount;i++){
        //cout << robot_list.front->r_type << endl;
        Robot* spawn_robot;
        if(robot_list.front->r_type == "RoboCop")
        {
            spawn_robot = new RoboCop(robot_list.front->r_x,robot_list.front->r_y,robot_list.front->r_name,A);
        }
        else if(robot_list.front->r_type == "Terminator")
        {
            spawn_robot = new Terminator(robot_list.front->r_x,robot_list.front->r_y,robot_list.front->r_name,A);
        }
        else if(robot_list.front->r_type == "SniperBot")
        {
            spawn_robot = new SniperBot(robot_list.front->r_x,robot_list.front->r_y,robot_list.front->r_name,A);
        }
        else if(robot_list.front->r_type == "TerminatorRobocop")
        {
            spawn_robot = new TerminatorRoboCop(robot_list.front->r_x,robot_list.front->r_y,robot_list.front->r_name,A);
        }
        else if(robot_list.front->r_type == "BlueThunder")
        {
            spawn_robot = new BlueThunder(robot_list.front->r_x,robot_list.front->r_y,robot_list.front->r_name,A);
        }
        else if(robot_list.front->r_type == "Madbot")
        {
            spawn_robot = new Madbot(robot_list.front->r_x,robot_list.front->r_y,robot_list.front->r_name,A);
        }
        else if(robot_list.front->r_type == "RoboTank")
        {
            spawn_robot = new RoboTank(robot_list.front->r_x,robot_list.front->r_y,robot_list.front->r_name,A);
        }
        else if(robot_list.front->r_type == "UltimateRobot")
        {
            spawn_robot = new UltimateRobot(robot_list.front->r_x,robot_list.front->r_y,robot_list.front->r_name,A);
        }
        else{cout << robot_list.front->r_type <<" Is not a valid robot type"<<endl;}
        cll.push(spawn_robot);
        robot_list.dequeue();
    }
    cout << endl << endl << endl;
    cout<<" $$$$$$$            $$\\                  $$\\          $$\\      $$\\                                      $$$$$$\\      $$$$$$\\  "<< endl;
    cout<<"$$  __$$           $$ |                 $$ |          $$ | $\\  $$ |                                    $$  __$$\\    $$$ __$$\\   "<< endl;
    cout<<"$$ |  $$ | $$$$$$\\  $$$$$$$\\   $$$$$$\\ $$$$$$\\        $$ |$$$\\ $$ | $$$$$$\\   $$$$$$\\   $$$$$$$\\       \\__/  $$ |   $$$$\\ $$ |  "<< endl;
    cout<<"$$$$$$$  |$$  __$$\\ $$  __$$\\ $$  __$$\\_$$  _|        $$ $$ $$\\$$ | \\____$$\\ $$  __$$\\ $$  _____|       $$$$$$  |   $$\\$$\\$$ |  "<< endl;
    cout<<"$$  __$$< $$ /  $$ |$$ |  $$ |$$ /  $$ | $$ |         $$$$  _$$$$ | $$$$$$$ |$$ |  \\__|\\$$$$$$\\        $$  ____/    $$ \\$$$$ |  "<< endl;
    cout<<"$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ | $$ |$$\\      $$$  / \\$$$ |$$  __$$ |$$ |       \\____$$\\       $$ |         $$ |\\$$$ |  "<< endl;
    cout<<"$$ |  $$ |\\$$$$$$  |$$$$$$$  |\\$$$$$$  | \\$$$$  |     $$  /   \\$$ |\\$$$$$$$ |$$ |      $$$$$$$  |      $$$$$$$$\\ $$\\$$$$$$  /  "<< endl;
    cout<<"\\__|  __| \\______/ \\_______/  \\______/   \\____/       \\__/     \\__| \\_______|\\__|      \\_______/       \\________|\\__|\\______/   "<< endl;
    cout << endl << endl << endl;
    cout << "Press To Start Simulation" << endl;
    cin.get();
    int option;
    bool picked = false;
    while(picked == false){
    cout <<endl<< "Which Gamemode would you like to play? "<<endl;
    cout<<"1. Normal Mode"<<endl;
    cout<<"2. Play with Rocks!(quicker simulation)"<<endl;
    cout<<"3. Play with Rocks and Rock Spawning(even QUICKER!)" <<endl;
    cin >> option;
    if(option == 1){picked=true;}
    else if(option == 2){picked=true;}
    else if(option == 3){picked=true;}
    else{cout << "Choose again"<<endl;}
    }
    if(option == 1){
    cll.simulate(A,robot_q);}
    else if(option == 2){
    A.spawnrocks();
    cll.simulate(A,robot_q);
    }
    else if(option == 3){
    A.spawnrocks();
    A.rock_setting = true;
    cll.simulate(A,robot_q);
    }

    return 0;
}
    
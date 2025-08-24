#include <iostream>
#include <string>
using namespace std;
int main(){
    string shape,command;
    bool state=true;
    int charchoice;
    
    cout<<"vacuum cleaner"<<endl;
    cout<<"enter character choice\n1-dust cleaner,\n2-rock cleaner,\n3-cloth cleaner,\n4-edge cleaner:";
    cin>>charchoice;
    if(charchoice==1){ 
    cout<<"dust cleaner selected,best shape circle"<<endl;}
    else if(charchoice==2){
     cout<<"rock cleaner selected,best shape square"<<endl;}
     else if(charchoice==3){
     cout<<"cloth cleaner selected,best shape rectangle"<<endl;}
     else if(charchoice==4){
     cout<<"cleaning dust at edges selected,best shape triangle"<<endl;
    }
    cout<<"enter shape(circle,square,rectangle,triangle):";
    cin>>shape;
   
    while(true){
    cout<<"enter command(start,stop,left,right,suck):";
    cin>>command;
    
    if(command=="start"){
        if(state){
            cout<<"started"<<endl;}
            else{
                cout<<"already started"<<endl;
            }
        }
        if(command=="left"){
            if(state){
                cout<<"moving left"<<endl;}
                else{
                    cout<<"please start the machine"<<endl;
                }
            }
        if(command=="right"){
            if(state){
                cout<<"moving right"<<endl;}
                else{
                    cout<<"please start the machine"<<endl;
                }
            }
            
     if(command=="suck"){
        if(state){
            if(shape=="circle"){
                cout<<"Circle: Best for cleaning fine dust like sand"<<endl;
        }
        else if(shape=="square"){
            cout<<"Square: Best for cleaning small rocks"<<endl;
        }
        else if(shape=="rectangle"){
            cout<<"Rectangle: Best for cleaning hair, cloth fibers, long threads"<<endl;
        }
        else if(shape=="triangle"){
            cout<<"Triangle: Best at cleaning corners and edges"<<endl;
        }
        cout<<"Sucking dirt, done!!"<<endl;
    }
    else{
        cout<<"Please start the machine"<<endl;
    }
}

    if(command=="stop"){
         if(state){
            cout<<"stopping"<<endl;
        }
        else{
            cout<<"already stopped"<<endl;
        }
    }
}}
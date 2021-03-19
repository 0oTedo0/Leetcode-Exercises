class ParkingSystem {
public:
    int mybig,mymedium,mysmall;
    ParkingSystem(int big, int medium, int small) {
        mybig=big;
        mymedium=medium;
        mysmall=small;
    }
    
    bool addCar(int carType) {
        switch(carType){
            case 1:
                if(mybig){
                    mybig--;
                    return true;
                }
                break;
            case 2:
                if(mymedium){
                    mymedium--;
                    return true;
                }
                break;
            case 3:
                if(mysmall){
                    mysmall--;
                    return true;
                }
                break;
        }
        return false;
    }
};

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem* obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj->addCar(carType);
 */

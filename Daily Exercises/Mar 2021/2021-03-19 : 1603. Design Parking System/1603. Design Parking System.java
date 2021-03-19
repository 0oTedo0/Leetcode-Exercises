class ParkingSystem {
    int mybig,mymedium,mysmall;
    public ParkingSystem(int big, int medium, int small) {
        mybig=big;
        mymedium=medium;
        mysmall=small;
    }
    
    public boolean addCar(int carType) {
        switch(carType){
            case 1:
                if(mybig>0){
                    mybig--;
                    return true;
                }
                break;
            case 2:
                if(mymedium>0){
                    mymedium--;
                    return true;
                }
                break;
            case 3:
                if(mysmall>0){
                    mysmall--;
                    return true;
                }
                break;
        }
        return false;
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem obj = new ParkingSystem(big, medium, small);
 * boolean param_1 = obj.addCar(carType);
 */

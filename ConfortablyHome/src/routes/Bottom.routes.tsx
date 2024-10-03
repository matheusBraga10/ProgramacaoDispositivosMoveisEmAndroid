import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import List from '../pages/list/Index';
import User from '../pages/user/Index';


const Tab = createBottomTabNavigator();

export default function BottomRoutes() {
  return (
    <Tab.Navigator>
      <Tab.Screen name="List" component={List} />
      <Tab.Screen name="User" component={User} />
    </Tab.Navigator>
  );
}
package widgets.FrClipAndShip.toc.tocClasses
{
	import flash.events.Event;

	public class MyOwnEvent extends Event
	{
		public static const RECEIVED_EVENT:String = "receivedEvent";
		//public String name;
		//public string message;		
		public var layerName:String;
		public var layerOn:String;
		
		public function MyOwnEvent (type:String, bubbles:Boolean = false, cancelable:Boolean = false)
		{
			// added per other post http://forums.adobe.com/thread/695571?tstart=0
			super(type);
		}

	}
}
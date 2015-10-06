// ActionScript file
package widgets.FrClipAndShip.toc.tocClasses
{	
	import flash.events.EventDispatcher;
	import mx.controls.Image;
	import mx.core.UIComponent;

	[Bindable]
	[RemoteClass(alias="widgets.FrClipAndShip.toc.tocClasses.LegendSymbolItem")]
	
	public class LegendSymbolItem extends EventDispatcher
	{
		public var label:String;
		public var image:Image;
		public var uic:UIComponent
	}
}
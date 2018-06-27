package  
{
	import flash.display.Sprite;
	import flash.display.StageDisplayState;
	import flash.display.StageScaleMode;
	import flash.events.MouseEvent;
	import flash.text.TextField;
	import flash.text.TextFieldAutoSize;

	[SWF(width = "512", height = "288")]
		
	/**
	 * ...
	 * @author Peter Backx
	 */
	public class StageScaleModeSample extends Sprite
	{
		[Embed(source = '../lib/tcw_512.jpg')]
		private var TestCard : Class;
		
		private var modeText : TextField;
		private var helpText : TextField;
		
		public function StageScaleModeSample() 
		{
			addChild(new TestCard());
			addChild(modeText = new TextField());
			
			modeText.background = true;
			modeText.autoSize = TextFieldAutoSize.LEFT;
			modeText.text = "current stage scale mode: " + stage.scaleMode;
			
			addChild(helpText = new TextField());
			helpText.background = true;
			helpText.autoSize = TextFieldAutoSize.LEFT;
			helpText.text = 
"this is a demonstration of the StageScaleMode property\n\
open this swf in a seperate window and resize it\n\
click on the mode display to change the StageScaleMode\n\
click on the window to go fullscreen\n\
click on this message to get started";
			helpText.x = 30;
			helpText.y = 30;
			
			helpText.addEventListener(MouseEvent.CLICK, removeHelp);
		}
		
		private function fullscreen(event:MouseEvent):void {
			stage.displayState = StageDisplayState.FULL_SCREEN;
		}
		
		private var modes:Array = new Array(StageScaleMode.EXACT_FIT, 
											StageScaleMode.NO_BORDER, 
											StageScaleMode.NO_SCALE, 
											StageScaleMode.SHOW_ALL);
		private var current:Number = 0;
											
		private function changeMode(event:MouseEvent):void {
			stage.scaleMode = modes[++current % 4];
			modeText.text = "current stage scale mode: " + stage.scaleMode;
			event.stopPropagation();
		}
		
		private function removeHelp(event:MouseEvent):void {
			removeChild(helpText);
			helpText.removeEventListener(MouseEvent.CLICK, removeHelp);
			event.stopPropagation();
			modeText.addEventListener(MouseEvent.CLICK, changeMode);
			stage.addEventListener(MouseEvent.CLICK, fullscreen);
		}
	}
	
}
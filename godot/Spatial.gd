extends Spatial

# Declare member variables here. Examples:
# var a = 2
# var b = "text"


# Called when the node enters the scene tree for the first time.
func _ready():
	# Create a timer node
	var timer = Timer.new()

	# Set timer interval
	timer.set_wait_time(1.0)

	# Set it as repeat
	timer.set_one_shot(false)

	# Connect its timeout signal to the function you want to repeat
	timer.connect("timeout", self, "getLastPosition")

	# Add to the tree as child of the current node
	add_child(timer)

	timer.start()


func getLastPosition():
	 $HTTPRequest.request("http://127.0.0.1:5000/last-position")

# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass


func _on_HTTPRequest_request_completed(result, response_code, headers, body):
	print(body.get_string_from_utf8())
	var data = JSON.parse(body.get_string_from_utf8())
	$cube.translation = Vector3(float(data.result["x"]),float(data.result["y"]),float(data.result["z"]))
	#$robot_skeleton.transform.translated(Vector3(float(data.result["x"]),float(data.result["y"]),float(data.result["z"])))
	pass # Replace with function body.
